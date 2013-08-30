# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand

from joomla.models import *
from data.models import *

def main():
    for joomla_course in JosOcwCourses.objects.all():
        print joomla_course
        provider, created = Provider.objects.get_or_create(
                name=joomla_course.source,
                defaults={
                    'external_id': joomla_course.crmid.id,
                    'active': True
                }
            )

        
        cforg = CfGetorgs.objects.get(crmid=joomla_course.crmid.id)

        source, created = Source.objects.get_or_create(
                provider = provider,
                kind = 'rss',
                url = cforg.url
        )

        course = Course.objects.create(
            title = joomla_course.title,
            linkhash = joomla_course.linkhash,
            linkurl = joomla_course.linkurl,
            provider = provider,
            source = source,
            description = joomla_course.description,
            tags = joomla_course.tags,
            language = joomla_course.language,
            author = joomla_course.author,
            rights = joomla_course.rights,
            contributors = joomla_course.contributors,
            license = joomla_course.license or '',

            date_published = joomla_course.date_published,
            date_indexed = joomla_course.date_indexed,
            date_modified = joomla_course.date_modified
        )

        print course.id

class Command(BaseCommand):
    args = ""
    help = "migrates joomla models to native ones"

    def handle(self, *args, **options):
        main()
