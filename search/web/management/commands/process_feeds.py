# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand

from web.models import *
from joomla.models import *

import hashlib
import feedparser
import datetime
from pprint import pprint

def main():
    m = hashlib.md5()

    for feed in CfGetorgs.objects.filter(executed=0):
        # if Course.objects.filter(source=feed).exists(): continue

        print feed.url
        d = feedparser.parse(feed.url)

        feed.last_indexed = datetime.datetime.now()
        feed.save()

        # first try a naive approach
        naive = False

        for entry in d.entries:
            # pprint(entry)
            #it's a normal rss
            if entry.get('link'):
                if not JosOcwCourses.objects.filter(linkurl=entry.link).exists() and entry.get('link'):
                    m.update(entry.link)
                    linkhash = m.hexdigest()

                    JosOcwCourses.objects.get_or_create(
                        crmid_id = feed.crmid,
                        linkhash = linkhash,
                        linkurl = entry.link,
                        title = entry.get('title'),
                        description = entry.get('description', ''),
                        source = feed.source,
                        language = feed.language,
                    )
            elif entry.get('rdf_li'):
                link = entry.id
                m.update(link)
                linkhash = m.hexdigest()
                JosOcwCourses.objects.get_or_create(
                    crmid_id = feed.crmid,
                    linkhash = linkhash,
                    linkurl = link,
                    defaults = {
                        'title': entry.title,
                        'description': entry.summary,
                        'source': feed.source,
                        'language': feed.language,
                        'author': entry.author,
                        'rights': entry.rights,
                        # 'license': entry.links[0].href,
                        'type': 'Course',
                        'format': 'text/html',
                        'level': 'Estudiante no licenciado',
                        'date_published': entry.updated_parsed,
                        'date_indexed': entry.updated_parsed,
                        'date_modified': entry.updated_parsed,
                        'locked': 0,
                        'enabled': True,
                    }
                )


            # course = Course.objects.get_or_create(
            #     source=feed, 
            #     permalink=entry.link,
            #     defaults={
            #         'title':entry.title,
            #         'description': entry.get('description')
            #     })

        
        # if naive: continue
        # print d.namespaces

        # no alternative approcahes for now

            

class Command(BaseCommand):
    help = "processes enabled feeds"

    def handle(self, *args, **options):
        main()
