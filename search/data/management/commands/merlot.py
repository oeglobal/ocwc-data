# -*- coding: utf-8 -*-
import xlwt
import requests
import requests_cache
import xml.etree.ElementTree as ET
from optparse import make_option
from collections import OrderedDict
from urlparse import urlsplit

from django.core.management.base import BaseCommand
from django.conf import settings

from data.models import Course, MerlotCategory

MERLOT_LANGUAGES = {
    'English': 1,
    'Arabic': 2,
    'Chinese': 3,
    'Czech': 4,
    'Danish': 5,
    'Dutch': 6,
    'French': 7,
    'German': 8,
    'Greek': 9,
    'Hebrew': 10,
    'Icelandic ': 11,
    'Italian': 12,
    'Japanese': 13,
    'Korean': 14,
    'Latin': 15,
    'Portuguese ': 16,
    'Russian': 17,
    'Spanish': 18,
    'Swedish': 19,
    'Turkish': 20,
    'Vietnamese': 21,
}

class Command(BaseCommand):
    help = "Utilities to merge our database with MERLOT"
    args = ""

    option_list = BaseCommand.option_list + (
        make_option("--subdomain-search", action="store", dest="subdomain_search", help="Searches arbitrary subdomain"),
        make_option("--import-categories", action="store_true", dest="import_categories", help="Imports Categories"),
        make_option("--export", action="store", dest="export_source", help="Export Source ID to Excel"),
        make_option("-f", action="store", dest="filename", help="Target filename")
    )

    def handle(self, *args, **options):
        if settings.DEBUG:
            requests_cache.install_cache('merlot')

        if options.get("subdomain_search"):
            self.subdomain_search(url=options.get("subdomain_search"))
            self.local_subdomain_search(url=options.get("subdomain_search"))
        elif options.get("import_categories"):
            self.import_categories()
        elif options.get("export_source"):
            self.export(source_id=options.get("export_source"), filename=options.get("filename"))

    def subdomain_search(self, url):
        print '-------- Present in MERLOT but missing in OEConsortium -------'
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
                    print '#######', material.find('URL').text, '\t\t\t', material.find('detailURL').text
                    self._locate_local_url(url)

                if params['page'] * 10 > num_results:
                    break
                
                params['page'] += 1
            else:
                break

    def local_subdomain_search(self, url):
        print '----- Missing in MERLOT but present in OEConsortium ------'
        for course in Course.objects.filter(linkurl__icontains=url, merlot_present=False, merlot_ignore=False):
            print course.linkurl

    def _locate_local_url(self, url):
        def __lookup_source(slug, source_id):
            try:
                course = Course.objects.get(linkurl__icontains=slug, source=source_id)
                if not course.merlot_present:
                    course.merlot_present = True
                    course.save()
                return course
            except Course.DoesNotExist:
                print "Missing:", url, slug
                return
            except Course.MultipleObjectsReturned:
                print "     -------"
                print "Too many results", url, slug
                for i in Course.objects.filter(linkurl__icontains=slug, source=source_id):
                    print i.id
                raise

        # Source: 8 - Johns Hopkins Bloomberg School of Public Health
        if url.startswith('http://ocw.jhsph.edu/'):
            slug = url.replace('http://ocw.jhsph.edu/courses', '').replace('/index.cfm', '')
            if slug[-1] != '/':
                slug += '/'
            return __lookup_source(slug, 8)
        
        # Source: 13 - Massachusetts Institute of Technology
        if url.startswith('http://ocw.mit.edu/'):
            if url.endswith('.htm'):
                r = requests.get(url, allow_redirects=True)
                url = r.url

            IGNORE_URLS = [
                'http://ocw.mit.edu/courses/physics/',
                'http://ocw.mit.edu/',
                'http://ocw.mit.edu',
                'http://ocw.mit.edu/courses/sloan-school-of-management/'
            ]
            if url in IGNORE_URLS:
                return

            IGNORE_FOLDERS = ['', 'textbook', 'proj', 'readings', 'sloan-school-of-management', 'projects']
            path = urlsplit(url).path.split('/')
            while path[-1] in IGNORE_FOLDERS:
                path.remove(path[-1])

            slug = path[-1]
            print ':::::', url, slug, url.split('/')[-1]
            return __lookup_source(slug, 13)

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

    def export(self, source_id, filename):
        wbk = xlwt.Workbook()
        sheet = wbk.add_sheet('Courses')

        first_row = OrderedDict([
            ('Title', 10),           # 0
            ('URL', 18),             # 1
            ('Mirror URL', 18),      # 2
            ('Description', 10),     # 3
            ('Image URL', 10),       # 4
            ('Material Type', 10),   # 5
            ('Audience', 10),        # 6
            ('Mobile OS Compatibility', 10),  # 7
            ('Material Version', 10),  # 8
            ('Technical Format', 10),   # 9
            ('Technical Requirements', 10),  # 10
            ('Source Code Available', 10),   # 11
            ('Accessibility Information Available', 10),  # 12
            ('Cost Involved', 10),    # 13
            ('Copyright', 10),        # 14
            ('Languages', 10),        # 15
            ('Category paths', 10),   # 16
            ('Submitter Username', 10),  # 17
            ('Author Username', 10),  # 18
            ('Author Name', 10),      # 19
            ('Author Email', 10),     # 20
            ('Author Org', 10),       # 21
            ('Creative Commons License: yes/no/unsure', 10),  # 22
            ('CC Commercial', 10),    # 23
            ('CC Derivatives', 10),   # 24
            ('Keywords', 10)          # 25
        ])

        r = c = 0

        for item in first_row:
            sheet.write(r, c, item)
            sheet.col(c).width = first_row[item] * 1000
            c += 1
        r += 1

        for course in Course.objects.filter(source_id=source_id, merlot_present=False, merlot_ignore=False):
            sheet.write(r, 0, course.title)
            sheet.write(r, 1, course.linkurl)
            # 2 empty - mirror url
            sheet.write(r, 3, course.description)
            sheet.write(r, 4, course.image_url)
            sheet.write(r, 5, 9)  # 9 - Online Course
            sheet.write(r, 6, 4)  # 4 - College General Ed
            # 7 - Mobile OS - empty
            # 8 - Material Version - empty
            if course.content_medium == 'video':
                sheet.write(r, 9, 20)  # 10 - Video
            else:
                sheet.write(r, 9, 10)  # 10 - HTML/Text
            # 10 - Technical requirements
            sheet.write(r, 11, 'Unsure')  # 11 - Source Code
            sheet.write(r, 12, 'Unsure')  # 12 - Accessibility
            sheet.write(r, 13, 'Unsure')  # 13 - Cost
            # 14 - Copyright
            sheet.write(r, 15, MERLOT_LANGUAGES[course.language])  # 15 - Language
            sheet.write(r, 16, course.get_merlot_categories())  # 16 - Category
            sheet.write(r, 17, 'oeconsortium')  # 17 - Submitter username
            # 18 - Author username
            authors = u';'.join(course.author.replace(', ', ',').split(','))
            sheet.write(r, 19, authors)  # 19 - Author name
            # 19 - Author Email
            # 20 - Author Org
            sheet.write(r, 22, course.creative_commons)
            if course.creative_commons_commercial == 'No':
                cc_commercial = 'false'
            elif course.creative_commons_commercial == 'Yes':
                cc_commercial = 'true'
            else:
                cc_commercial = ''
            sheet.write(r, 23, cc_commercial)
            sheet.write(r, 24, course.creative_commons_derivatives)

            tags = u';'.join(course.tags.replace(', ', ',').split(',') + ['oec', 'ocwc'])
            sheet.write(r, 25, tags)  # 25 - Keywords

            r += 1
        wbk.save(filename)

        self.stdout.write("Wrote %s courses to %s" % (r, filename))
