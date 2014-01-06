# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from django.conf import settings
from web.models import *
from joomla.models import *

import json
import os
import hashlib

def main(crmid=None):    
    if crmid:
        filename_list = ['scraped/%s.json' % crmid]
    else:
        filename_list = ['scraped/'+str(x) for x in os.listdir('scraped')]

    for f in filename_list:
        path, filename = os.path.split(f)
        crmid = filename.split('.')[0]

        print "Importing", crmid, path, filename
        JosOcwCourses.objects.filter(crmid=crmid).delete()

        contact = CivicrmContact.objects.get(pk=crmid)

        raw_data = open(f).readlines()
        for raw_entry in raw_data:
            entry = json.loads(raw_entry)
            link = entry.get('url')
            linkhash = hashlib.md5(link.encode('utf-8')).hexdigest()

            JosOcwCourses.objects.create(
                crmid_id = crmid,
                linkhash = linkhash,
                linkurl = link,
                title = ''.join(entry.get('title','')),
                description = entry.get('description', ''), #.replace('\r\n', '<br />'),
                tags = ', '.join(entry.get('categories','')),
                source = contact.legal_name,
                author = ','.join(entry.get('author')),
                language = 'English',
                enabled = 1
            )         


class Command(BaseCommand):
    args = "<crmid>"
    help = "imports scraped .json into main database - takes json filename as argument"

    def handle(self, *args, **options):
        if args:
            for crmid in args:
                main(crmid)
        else:
            main()
