# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand

from joomla.models import *
from web.models import *


CiviInst = CivicrmValue1InstitutionInformation
def main():
    # for item in CiviInst.objects.filter(rss_course_feed__isnull=False):
    #     if item.rss_course_feed.startswith('http') and bool(item.ocw_site_approved):
    #         if not CourseFeed.objects.filter(url=item.rss_course_feed).exists():
    #             feed = CourseFeed.objects.create(
    #                 source=item.entity.display_name,
    #                 crm_id=item.entity.id,
    #                 url=item.rss_course_feed,
    #                 language=item.rss_course_feed_language,
    #                 enabled=False,
    #                 reviewed=False)

    for item in CfGetorgs.objects.all():
        # print item.crmid, item.url
        if CourseFeed.objects.filter(crm_id=item.crmid).exists():
            feed = CourseFeed.objects.get(crm_id=item.crmid)
            if not item.url == feed.url:
                print item.crmid, item.url
        else:
            print item.crmid, item.url

class Command(BaseCommand):
    help = "copies feeds from civicrm to our django app"

    def handle(self, *args, **options):
        main()
