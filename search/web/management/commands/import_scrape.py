# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand

from web.models import *
from joomla.models import *

import json
import os
import hashlib

def main():
    m = hashlib.md5()
    filename_list = ['scraped/693.json',]

    for f in filename_list:
        path, filename = os.path.split(f)
        crmid = filename.split('.')[0]

        contact = CivicrmContact.objects.get(pk=crmid)

        data = json.loads(open(f).read())
        for entry in data:
            link = entry.get('url')
            m.update(link)
            linkhash = m.hexdigest()

            JosOcwCourses.objects.get_or_create(
                crmid_id = crmid,
                linkhash = linkhash,
                linkurl = link,
                title = ''.join(entry.get('title','')),
                description = entry.get('description', ''), #.replace('\r\n', '<br />'),
                source = contact.legal_name,
                author = ','.join(entry.get('author')),
                language = 'English',
                enabled = 1
            )         


class Command(BaseCommand):
    help = "imports scraped .json into main database - takes json filename as argument"

    def handle(self, *args, **options):
        main()
