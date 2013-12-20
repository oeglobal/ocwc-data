# -*- coding: utf-8 -*-
import json
import requests
from requests.auth import HTTPBasicAuth
from optparse import make_option

from django.core.management.base import BaseCommand
from django.conf import settings

import data.models
from data.models import Course, Provider, Source

class Command(BaseCommand):
    help = "Download list of feeds from OCW members portal and compares it with local providers list"
    args = "--list --add id"

    option_list = BaseCommand.option_list + (
        make_option("--list", action="store_true", dest="list-providers", help="List providers that are new/different (default)"),
        make_option("--add", action="store", dest="provider-id", help="ID of provider to add to the search system")
    )

    def handle(self, *args, **options):
        if options.get("provider-id"):
            self.add_provider(options.get("provider-id"))
        else:
            self.list_providers()

    def add_provider(self, provider_id):
        r = requests.get('http://members.ocwconsortium.org/api/v1/organization/feeds/?format=json',
                         auth=HTTPBasicAuth(settings.MEMBERS_API_USERNAME, settings.MEMBERS_API_PASSWORD))
        feeds_list = json.loads(r.content)

        for item in feeds_list:
            if item.get('id') == int(provider_id):
                provider, is_created = Provider.objects.get_or_create(
                    name=item.get('name'),
                    external_id=provider_id
                )

                source, is_created = Source.objects.get_or_create(
                    provider=provider,
                    kind='rss',
                    url=item.get('rss_course_feed')
                )

                print 'Added new provider', source

                break

    def list_providers(self):
        r = requests.get('http://members.ocwconsortium.org/api/v1/organization/feeds/?format=json',
                         auth=HTTPBasicAuth(settings.MEMBERS_API_USERNAME, settings.MEMBERS_API_PASSWORD))
        feeds_list = json.loads(r.content)

        for item in feeds_list:
            crmid = item.get('crmid')
            rss_course_feed = item.get('rss_course_feed')

            try:
                provider = Provider.objects.get(external_id='crmid:'+crmid)
            except Provider.DoesNotExist:
                try:
                    provider = Provider.objects.get(external_id=item.get('id'))
                except Provider.DoesNotExist:
                    print "New provider: %s (crmid:%s) %s %s" % (item.get('id'), crmid, item.get('name'), rss_course_feed)
                    print '\n',
                    continue

            if not provider.source_set.filter(url=rss_course_feed, kind='rss'):
                print "Provider (%s) %s is missing feed: %s" % (provider.id, provider.name, rss_course_feed)

                for source in provider.source_set.all():
                    print "\t (%s) %s: %s" % (source.id, source.kind, source.url)
                print '\n',