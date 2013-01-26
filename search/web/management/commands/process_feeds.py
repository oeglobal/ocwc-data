# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand

from web.models import *
from joomla.models import *

import hashlib
import feedparser

def main():
    m = hashlib.md5()

    for feed in CourseFeed.objects.filter(enabled=True):
        # if Course.objects.filter(source=feed).exists(): continue

        print feed.url      
        d = feedparser.parse(feed.url)

        # first try a naive approach
        naive = False
        for entry in d.entries:
            if not JosOcwCourses.objects.filter(linkurl=entry.link).exists() and entry.get('link'):
                print entry.link
                m.update(entry.link)
                linkhash = m.hexdigest()

                JosOcwCourses.objects.get_or_create(
                    crmid = feed.crmid,
                    linkhash = linkhash,
                    linkurl = entry.link,
                    title = entry.get('title'),
                    description = entry.get('description', ''),
                    source = feed.source,
                    language = feed.language,
                )



            # course = Course.objects.get_or_create(
            #     source=feed, 
            #     permalink=entry.link,
            #     defaults={
            #         'title':entry.title,
            #         'description': entry.get('description')
            #     })

            naive = True
        
        # if naive: continue
        # print d.namespaces

        # no alternative approcahes for now

            

class Command(BaseCommand):
    help = "processes enabled feeds"

    def handle(self, *args, **options):
        main()
