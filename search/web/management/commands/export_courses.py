# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand

from joomla.models import *
from web.models import *

import xlwt

def main(filename):
    wbk = xlwt.Workbook()
    sheet = wbk.add_sheet('Courses')

    excel_date_fmt = 'D.M.Y'
    style = xlwt.XFStyle()
    style.num_format_str = excel_date_fmt


    first_row = ['Hash', 'Link', 'Source', 'Language', 'Tags', 'Author', 'Title', 'Description', 'Published', 'Indexed', 'Modified', 'Lat,long']
    r = c = 0

    for item in first_row:
        sheet.write(r, c, item)
        sheet.col(c).width = 2024 * len(item)
        c += 1
    r += 1

    for course in JosOcwCourses.objects.all():
        link = 'HYPERLINK("http://www.ocwconsortium.org/en/courses/browsesource/course/%s"; "%s")' % (course.linkhash, course.linkhash)

        address = course.crmid.civicrmaddress_set.all()[0]
        lat_long = "%s,%s" % (address.geo_code_1, address.geo_code_2)

        sheet.write(r,  0, xlwt.Formula(link))
        sheet.write(r,  1, course.linkurl)
        sheet.write(r,  2, course.source)
        sheet.write(r,  3, course.language)
        sheet.write(r,  4, course.tags)
        sheet.write(r,  5, course.author)
        sheet.write(r,  6, course.title)
        sheet.write(r,  7, course.description)
        sheet.write(r,  8, course.date_published, style)
        sheet.write(r,  9, course.date_indexed,   style)
        sheet.write(r, 10, course.date_modified,  style)
        sheet.write(r, 11, lat_long)

        r += 1

    sheet = wbk.add_sheet('Members')

    first_row = ['CRM ID', 'Display name', 'Joined date', 'Lat,long', 'City']
    r = c = 0

    for item in first_row:
        sheet.write(r, c, item)
        sheet.col(c).width = 2024 * len(item)
        c += 1
    r += 1

    for member in CivicrmMembership.objects.filter(status__in=[2,3,5,7]):
        address = None
        if member.contact.civicrmaddress_set.count():
            address = member.contact.civicrmaddress_set.all()[0]
            lat_long = "%s,%s" % (address.geo_code_1, address.geo_code_2)

        sheet.write(r, 0, member.contact.id)
        sheet.write(r, 1, member.contact.display_name)
        sheet.write(r, 2, member.join_date, style)
        if address:
            sheet.write(r, 3, lat_long)
            sheet.write(r, 4, address.city)

        r += 1

    wbk.save(filename)

class Command(BaseCommand):
    args = "filename.xls"
    help = "processes enabled feeds"

    def handle(self, *args, **options):
        for filename in args:
            main(filename)
