# -*- coding: utf-8 -*-
import hashlib
import requests
from optparse import make_option

from django.core.management.base import BaseCommand

from data.models import Course

class Command(BaseCommand):
    help = "One time mantainance operation on data models"
    args = "--fix-hashes"

    option_list = BaseCommand.option_list + (
        make_option("--fix-hashes", action="store_true", dest="fix_hashes", help="Regenerates linkhash and removes duplicates"),
        make_option("--check-404", action="store_true", dest="check_404", help="Checks for 404 links")
    )

    def handle(self, *args, **options):
        if options.get('fix_hashes'):
            self.fix_hashes()
        if options.get('check_404'):
            self.check_broken_links()

    def fix_hashes(self):
        # remove wrongly calculated hashes and generate new ones
        for course in Course.objects.order_by('-id'):
          digest = hashlib.md5(course.linkurl.encode('utf-8')).hexdigest()

          if digest != course.linkhash:
              try:
                  Course.objects.get(linkhash=digest)
                  course.delete()
              except Course.DoesNotExist:
                  print 'new digest for', [course.title]
                  course.linkhash = digest
                  course.save()

    def check_broken_links(self):
        for course in Course.objects.filter(is_404=False, merlot_url='', source__isnull=False).order_by('source'):
            print(course.id, course.linkurl)
            r = requests.get(course.linkurl)
            if r.status_code == 404:
                print(u'Removing: {} - {} ({})'.format(course.source.provider.name, course.title, course.linkurl))

                course.is_404 = True
                course.save()
            else:
                print('OK {}'.format(course.linkurl))
