# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand

from optparse import make_option

from data.models import Source, Course


class Command(BaseCommand):
    help = "Utility function to fix certain old sources"
    args = "--update-source [id]"

    option_list = BaseCommand.option_list + (
        make_option("--update-source", action="store", dest="update_source", help="Update specific source"),
    )

    def handle(self, *args, **options):
        if options.get('update_source'):
            source_id = options.get('update_source')

            # The Johns Hopkins University
            if int(source_id) == 8:
                self.fix_jhsph()

    def fix_jhsph(self):
        source = Source.objects.get(pk=8)

        for url in open('dumps/008_jhsph_remote.txt').read().splitlines():
            slug = url.replace('http://ocw.jhsph.edu/index.cfm/go/viewCourse/course/', '').replace('/coursePage/index/', '')
            # print slug

            try:
                course = Course.objects.get(source=source, linkurl__icontains=slug + "?source=rss")
            except Course.DoesNotExist:
                try:
                    course = Course.objects.get(source=source, linkurl__icontains="/" + slug + "/")
                except Course.DoesNotExist:
                    print "missing", url
                    continue

            course.linkurl = url
            course.save(update_linkhash=True)
