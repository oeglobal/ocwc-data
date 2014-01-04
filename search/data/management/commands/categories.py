# -*- coding: utf-8 -*-
from optparse import make_option
from pprint import pprint
from collections import OrderedDict
import requests
import json
import xlwt

from django.core.management.base import BaseCommand
from django.conf import settings

from data.models import Course

class Command(BaseCommand):
    help = "Experimental commands that are use to build course catalog"
    args = "--opencalais"

    option_list = BaseCommand.option_list + (
        make_option("--opencalais", action="store_true", dest="opencalais", help="Runs OpenCalais matching"),
        make_option("--xls", action="store", dest="xls_filename", help="Debug XLS"),
        make_option("--txt", action="store", dest="txt_folder", help="TXT Store for OptiGen"),
    )

    def handle(self, *args, **options):
        if options.get("opencalais"):
            self.calculate_smart_tags()
        if options.get("xls_filename"):
            self.export_debug_xls(options.get("xls_filename"))
        if options.get('txt_folder'):
            self.export_documents(options.get('txt_folder'))

    def calculate_smart_tags(self):
        ENDPOINT = 'http://api.opencalais.com/tag/rs/enrich'

        headers = {'x-calais-licenseID': settings.OPENCALAIS_API_KEY,
                   'Content-Type': 'text/html',
                   'Accept': 'application/json',
                   'enableMetadataType': 'SocialTags'}

        for course in Course.objects.filter(language='English', opencalais_response='').extra(where=["CHAR_LENGTH(description) > 300"])[:150]:
            print course.title
            print course.description
            print '-'*20

            content = {'content': u"%s %s" % (course.title, course.description) }
            r = requests.post(ENDPOINT, content, headers=headers)
            data = json.loads(r.content)

            socialtags = []
            topics = []
            for i in data:
                item = data[i]
                if item.get('_typeGroup') == 'socialTag':
                    socialtags.append(item.get('name').replace('_', ' '))
                if item.get('_typeGroup') == 'topics':
                    topics.append(item.get('categoryName').replace('_', ' '))


            course.calais_socialtags = ', '.join(socialtags)
            course.calais_topics = ', '.join(topics)
            course.opencalais_response = r.content
            course.save()

    def export_debug_xls(self, xls_filename):
        wbk = xlwt.Workbook()
        sheet = wbk.add_sheet('Courses')

        first_row = OrderedDict([
            ('OCW Link', 18000),    # 0
            ('Link', 20000),        # 1
            ('Provider', 8000),     # 2
            ('Title', 10000),       # 3
            ('Description', 10000), # 4
            ('SocialTags', 8000),   # 5
            ('Topics', 8000),       # 6
        ])

        r = c = 0

        for item in first_row:
            sheet.write(r, c, item)
            sheet.col(c).width = first_row[item]
            c += 1
        r += 1

        link = 'http://www.ocwconsortium.org/courses/view/%s/'

        for course in Course.objects.exclude(calais_socialtags=''):
                sheet.write(r, 0, link % course.linkhash )
                sheet.write(r, 1, course.linkurl )
                sheet.write(r, 2, course.provider.name )
                sheet.write(r, 3, course.title )
                sheet.write(r, 4, course.description )
                sheet.write(r, 5, course.calais_socialtags )
                sheet.write(r, 6, course.calais_topics )

                r += 1

        wbk.save(xls_filename)
        self.stdout.write("Wrote %s courses to %s" % (r, xls_filename))

    def export_documents(self, folder):
        # for course in Course.objects.filter(language='English', opencalais_response='').extra(where=["CHAR_LENGTH(description) > 300"])[:150]:
        for course in Course.objects.exclude(calais_socialtags=''):
            f = open('%s/%s.txt' % (folder, course.id), 'w')
            f.write(course.title.encode('utf-8')+'\n')
            f.write(course.description.encode('utf-8'))
            f.close()
