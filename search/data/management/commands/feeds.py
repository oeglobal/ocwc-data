# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand

import hashlib
import feedparser
import datetime
from optparse import make_option

from data.models import Course, Source

m = hashlib.md5()

class Command(BaseCommand):
    help = "Manage RSS feeds that are defined in Sources for Providers"
    args = "--update-all --update-source [id]"

    option_list = BaseCommand.option_list + (
        make_option("--update-all", action="store_true", dest="update_all", help="Fetches all RSS feeds"),
        make_option("--update-source", action="store", dest="update_source", help="Fetches specific RSS feed"),
    )

    def handle(self, *args, **options):
        if options.get('update_all'):
            self.update_all()
        if options.get('update_source'):
            self.update_source(source_id=options.get('update_source'))

    def update_all(self):
        self.stdout.write("Downloading all feeds")

        for source in Source.objects.filter(kind='rss'):
            self.update_source(source=source)

    def update_source(self, source_id=None, source=None):
        if not source:
            source = Source.objects.get(pk=source_id)
        self.stdout.write("Source: %s - %s" % (source.id, source.url))

        d = feedparser.parse(source.url)
        for entry in d.entries:
            #it's a normal rss
            if entry.get('link'):
                m.update(entry.link)
                linkhash = m.hexdigest()

                course, created = Course.objects.get_or_create(
                    linkhash = linkhash,
                    linkurl = entry.link,
                    defaults={
                        'title': entry.get('title'),
                        'description': entry.get('description', ''),
                        'provider': source.provider,
                        'source': source,
                        'language': 'English',
                    }
                )
            else:
                link = entry.id
                m.update(link)
                linkhash = m.hexdigest()
                course, created = Course.objects.get_or_create(
                    linkhash = linkhash,
                    linkurl = link,
                    defaults = {
                        'title': entry.title,
                        'description': entry.summary,
                        'provider': source.provider,
                        'source': source,
                        'language': 'English',
                        'author': entry.author,
                        'rights': entry.rights,
                        'date_published': entry.updated_parsed,
                        'date_indexed': entry.updated_parsed,
                        'date_modified': entry.updated_parsed
                    }
                )

            if created:
                self.stdout.write("Created: %s - %s" % (course.id, course.title))
            else:
                self.stdout.write("Already seen course: %s - %s" % (course.id, course.title))