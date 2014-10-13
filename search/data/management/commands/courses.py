# -*- coding: utf-8 -*-
from optparse import make_option
from django.core.management.base import BaseCommand

from messytables import XLSTableSet, headers_guess, headers_processor, offset_processor

from data.models import Source, Course, MerlotCategory

class Command(BaseCommand):
    help = "Utilities to merge our database with MERLOT"
    args = "--file"

    option_list = BaseCommand.option_list + (
        make_option("--file", action="store", dest="filename", help="Source filename"),
        make_option("--source", action="store", dest="source_id", help="Source ID"),
        make_option("--provider", action="store", dest="provider_tag", help="Provider Tag"),
    )

    def handle(self, *args, **options):
        if options.get('filename'):
            self.ku_openlearning(options.get('filename'), options.get('source_id'))

    def ku_openlearning(self, filename, source_id):
        CATEGORY_MAPPING = {
            'Assessment of learning': 2298, #Assessment,
            'Finance': 2235,
            'Public Service': 'Criminal Justice',
            'Health Science': 'Health Sciences',
            'Management': 2248,
            'Online Instruction': 'Hybrid and Online Course Development',
            'Early Childhood': ['Career Counseling and Services', 'Childhood and Adolescence'],
            'Law, Legal': 'Law',
            'Psychology': 'Psychology',
            'Customer Service': 2246,
            'Communications': 'Communications',
            'Professionalism': 'Personal Development'
        }

        source = Source.objects.get(pk=source_id)

        fh = open(filename, 'rb')
        table_set = XLSTableSet(fh)

        row_set = table_set.tables[0]
        offset, headers = headers_guess(row_set.sample)
        row_set.register_processor(headers_processor(headers))

        row_set.register_processor(offset_processor(offset + 1))
        for row in row_set:
            url = row[0].value
            title = row[1].value
            description = row[2].value
            # language = row[4].value
            # material_type = row[5].value
            license = row[6].value
            categories = row[7].value
            keywords = row[8].value
            # audience = row[9].value

            course, is_created = Course.objects.get_or_create(
                linkurl = url,
                provider = source.provider,
                source = source,
                
                defaults = {
                    'title': title,
                    'description': description,
                    'tags': keywords,
                    'language': 'English',
                    'license': license,
                    'content_medium': 'text',
                    'creative_commons': 'Yes',
                    'creative_commons_commercial': 'No',
                    'creative_commons_derivatives': 'No'
                    }
                )

            merlot_cat = CATEGORY_MAPPING[categories]
            if type(merlot_cat) != list:
                merlot_cat = [merlot_cat,]

            for item in merlot_cat:
                try:
                    m = MerlotCategory.objects.get(merlot_id=item)
                    course.merlot_categories.add(m)
                except ValueError:
                    m = MerlotCategory.objects.get(name=item)
                    course.merlot_categories.add(m)
