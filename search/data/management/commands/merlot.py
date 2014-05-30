# -*- coding: utf-8 -*-
import requests
import requests_cache
import xml.etree.ElementTree as ET
from optparse import make_option

from django.core.management.base import BaseCommand
from django.conf import settings

from data.models import Course, MerlotCategory


class Command(BaseCommand):
    help = "Utilities to merge our database with MERLOT"
    args = ""

    option_list = BaseCommand.option_list + (
        make_option("--subdomain-search", action="store", dest="subdomain_search", help="Searches arbitrary subdomain"),
        make_option("--import-categories", action="store_true", dest="import_categories", help="Imports Categories")
    )

    def handle(self, *args, **options):
        if settings.DEBUG:
            requests_cache.install_cache('merlot')

        if options.get("subdomain_search"):
            self.subdomain_search(url=options.get("subdomain_search"))
            self.local_subdomain_search(url=options.get("subdomain_search"))
        elif options.get("import_categories"):
            self.import_categories()

    def subdomain_search(self, url):
        print '-------- MERLOT -------'
        params = {
            'licenseKey': settings.MERLOT_KEY,
            'page': 1,
            'url': url
        }

        while True:
            r = requests.get(settings.MERLOT_API_URL + '/materialsAdvanced.rest', params=params)
            
            tree = ET.fromstring(r.content)
            
            num_results = int(tree.find('nummaterialstotal').text)

            if num_results > 0:
                for material in tree.findall('material'):
                    url = material.find('URL').text
                    # print material.find('URL').text, '\t\t\t', material.find('detailURL').text
                    self._locate_local_url(url)

                if params['page'] * 10 > num_results:
                    break
                
                params['page'] += 1
            else:
                break

    def local_subdomain_search(self, url):
        print '----- OEConsortium ------'
        for course in Course.objects.filter(linkurl__icontains=url, merlot_present=False):
            print course.linkurl

    def _locate_local_url(self, url):
        # Source: 8 - Johns Hopkins Bloomberg School of Public Health
        if url.startswith('http://ocw.jhsph.edu/'):
            slug = url.replace('http://ocw.jhsph.edu/courses', '').replace('/index.cfm', '')
            if slug[-1] != '/':
                slug += '/'

            try:
                course = Course.objects.get(linkurl__icontains=slug, source=8)
                if not course.merlot_present:
                    course.merlot_present = True
                    course.save()
            except Course.DoesNotExist:
                print "Missing:", url, slug
                return
            except Course.MultipleObjectsReturned:
                print "Too many results", url, slug
                return

    def import_categories(self):
        def _get_children(parent_category, depth=0):
            for category in list(parent_category):
                if category.attrib.get('id'):
                    if depth > 0:
                        parent = MerlotCategory.objects.get(merlot_id=parent_category.attrib.get('id'))
                    else:
                        parent = None

                    MerlotCategory.objects.get_or_create(merlot_id=category.attrib.get('id'),
                                                        defaults={
                                                            'name': category.find('name').text,
                                                            'parent': parent
                                                        })
                if list(category):
                    _get_children(category, depth + 1)

        params = {
            'licenseKey': settings.MERLOT_KEY,
        }
        r = requests.get(settings.MERLOT_API_URL + '/categories.rest', params=params)

        tree = ET.fromstring(r.content)
        _get_children(tree, 0)
