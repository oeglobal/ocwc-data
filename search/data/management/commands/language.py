# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand

from optparse import make_option
import cld

from data import LANG_MAPPING
from data.models import Course

class Command(BaseCommand):
    help = "Detects languages inside Courses"
    args = "--update-all"

    option_list = BaseCommand.option_list + (
        make_option("--update-all", action="store_true", dest="update_all", help="Detects languages on all courses"),
    )

    def handle(self, *args, **options):
        if options.get('update_all'):
            self.update_all()

    def update_all(self):
    	for course in Course.objects.filter(language__iexact="english"):
                topLanguageName, topLanguageCode, isReliable, textBytesFound, details = cld.detect(course.title.encode('utf-8') + " " + course.description.encode('utf-8'))
                if topLanguageCode not in  ['en','un']:
                    # force unidentified languages into English
                    if topLanguageCode == 'un':
                        topLanguageName = 'English'

                    language = topLanguageName.lower().capitalize()
                    if language in LANG_MAPPING:
                        course.language = language
                        course.save()
                        continue
                    else:
                    	self.stdout.write("New language %s %s %s" % (topLanguageName, topLanguageCode, isReliable))
