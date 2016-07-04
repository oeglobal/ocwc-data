# -*- coding: utf-8 -*-
import xlwt
from optparse import make_option
from collections import OrderedDict

from django.core.management.base import BaseCommand

from data.models import Provider

class Command(BaseCommand):
    help = "Exports list of OCW courses to XLS and TSV"
    args = "--xls <file> --tsv <file>"

    option_list = BaseCommand.option_list + (
        make_option("--xls", action="store", dest="xls_filename", help="XLS filename"),
    )

    def handle(self, *args, **options):
        if options.get("xls_filename"):
            self.export_xls(options.get("xls_filename"))

    def export_xls(self, xls_filename):
        wbk = xlwt.Workbook()
        sheet = wbk.add_sheet('Courses')

        excel_date_fmt = 'D.M.Y'
        style = xlwt.XFStyle()
        style.num_format_str = excel_date_fmt

        first_row = OrderedDict([
            ('OCW Link', 18000),    # 0
            ('URL Hash', 8000),     # 1
            ('Link', 20000),        # 2
            ('Provider', 8000),     # 3
            ('Language', 5000),     # 4
            ('Tags', 8000),         # 5
            ('Author', 8000),       # 6
            ('Title', 10000),       # 7
            ('Description', 10000), # 8
            ('Published', 5000),    # 9
            ('Indexed', 5000),      # 10
            ('Modified', 5000),     # 11
            ('Categories', 10000)   # 12
        ])

        r = c = 0

        for item in first_row:
            sheet.write(r, c, item)
            sheet.col(c).width = first_row[item]
            c += 1
        r += 1

        link = 'http://www.ocwconsortium.org/courses/view/%s/'

        for provider in Provider.objects.all():
            for source in provider.source_set.active():
                for course in source.course_set.all():

                    sheet.write(r, 0, link % course.linkhash)
                    sheet.write(r, 1, course.linkhash)
                    sheet.write(r, 2, course.linkurl)
                    sheet.write(r, 3, provider.name)
                    sheet.write(r, 4, course.language)
                    sheet.write(r, 5, course.tags)
                    sheet.write(r, 6, course.author)
                    sheet.write(r, 7, course.title)
                    sheet.write(r, 8, course.description[:32760])
                    sheet.write(r, 9, course.date_published, style)
                    sheet.write(r, 10, course.date_indexed, style)
                    sheet.write(r, 11, course.date_modified, style)

                    cat_tree = []
                    for cat in course.merlot_categories.all():
                        cat_tree.append('/'.join( ['All'] + map( unicode, cat.get_ancestors() ) + [cat.name] ) )
                    sheet.write(r, 12, ';'.join(cat_tree))

                    r += 1

        wbk.save(xls_filename)
        self.stdout.write("Wrote %s courses to %s" % (r, xls_filename))
