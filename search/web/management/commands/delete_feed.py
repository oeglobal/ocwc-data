# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand

from web.models import *
from joomla.models import *

import sys

def main():
    crmid = sys.argv[2]
    delete = False
    if len(sys.argv) == 4:
        if sys.argv[3] == 'delete':
            delete = True
            print 'deleting:'

    # for feed in CfGetorgs.objects.filter(crmid=crmid):
    #   print feed.source
    #   if delete:
    #       feed.delete()

    for item in JosOcwCourses.objects.filter(crmid=crmid):
        print [item.title]
        if delete:
            item.delete()


class Command(BaseCommand):
    help = "deletes feed from url list and any downloaded items"

    def handle(self, *args, **options):
        main()
