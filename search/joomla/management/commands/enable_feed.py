# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand

from web.models import *
from joomla.models import *

import sys

def main():
    crmid = sys.argv[2]

    print "Enabling all courses in", crmid
    for item in JosOcwCourses.objects.filter(crmid=crmid):
        print [item.title]
        item.enabled = True
        item.save()

class Command(BaseCommand):
    help = "deletes feed from url list and any downloaded items"

    def handle(self, *args, **options):
        main()
