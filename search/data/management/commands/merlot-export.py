# -*- coding: utf-8 -*-
import xlwt
from optparse import make_option
from collections import OrderedDict

from django.core.management.base import BaseCommand

from data.models import Source


class Command(BaseCommand):
    help = "Exports list of OCW courses to XLS that can be imported into MERLOT"
    args = "--xls <file>"

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
            ('Title', 10000),           # 0
            ('URL', 18000),             # 1
            ('Mirror URL', 18000),      # 2
            ('Description', 10000),     # 3
            ('Image URL', 10000),       # 4
            ('Material Type', 10000),   # 5
            ('Audience', 10000),        # 6
            ('Mobile OS Compatibility', 10000),  # 7
            ('Material Version', 10000),  # 8
            ('Technical Format', 1000),   # 9
            ('Technical Requirements', 1000),  # 10
            ('Source Code Available', 1000),   # 11
            ('Accessibility Information Available', 1000),  # 12
            ('Cost Involved', 1000),    # 13
            ('Copyright', 1000),        # 14
            ('Languages', 1000),        # 15
            ('Category paths', 1000),   # 16
            ('Submitter Username', 1000),  # 17
            ('Author Username', 1000),  # 18
            ('Author Name', 1000),      # 19
            ('Author Email', 1000),     # 20
            ('Author Org', 1000),       # 21
            ('Creative Commons License: yes/no/unsure', 1000),  # 22
            ('CC Commercial', 1000),    # 23
            ('CC Derivatives', 1000),   # 24
            ('Keywords', 1000)          # 25
        ])

        r = c = 0

        for item in first_row:
            sheet.write(r, c, item)
            sheet.col(c).width = first_row[item]
            c += 1
        r += 1

        for course in Source.objects.get(pk=8).course_set.all():
            sheet.write(r, 0, course.title)
            sheet.write(r, 1, course.linkurl)
            # 2 empty
            sheet.write(r, 3, course.description)
            # 4 empty
            sheet.write(r, 5, 9)  # 9 - Online Course
            sheet.write(r, 6, 4)  # 4 - College General Ed
            # 7 - Mobile OS
            # 8 - Material Version
            sheet.write(r, 9, 10)  # 10 - HTML/Text*
            # 10 - Technical requirements
            # 11 - Source Code
            # 12 - Accessibility
            # 13 - Cost
            # 14 - Copyright
            sheet.write(r, 15, 1)  # 1 - English
            # 16 - Category
            sheet.write(r, 17, 'oeconsortium')

            r += 1
        wbk.save(xls_filename)

        self.stdout.write("Wrote %s courses to %s" % (r, xls_filename))
