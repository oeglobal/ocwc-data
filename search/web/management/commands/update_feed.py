# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand

from joomla.models import *
from web.models import *

def main(crmid):
    institution = CivicrmValue1InstitutionInformation.objects.get(entity_id=crmid)
    if CfGetorgs.objects.filter(crmid=institution.entity_id).exists():
        feed = CfGetorgs.objects.get(crmid=institution.entity_id)

        print "Updated", crmid, '\n\tfrom', feed.url, '\n\tto', institution.rss_course_feed

        feed.url = institution.rss_course_feed
        feed.save()

    else:
        contact = CivicrmContact.objects.get(pk=crmid)
        feed = CfGetorgs.objects.create(
            source=contact.legal_name,
            crmid=crmid,
            url=institution.rss_course_feed,
            language='English'
        )

        print 'Added', contact.legal_name, 'and language English. Please check the language.'

class Command(BaseCommand):
    args = "<crmid crmid crmid ...>"
    help = "updates feed from CRM to CfGetorgs"

    def handle(self, *args, **options):
        for crmid in args:
            main(crmid)
