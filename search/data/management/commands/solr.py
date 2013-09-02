# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from django.conf import settings

from optparse import make_option
import pysolarized

from data import LANG_MAPPING
from data.models import Course

class Command(BaseCommand):
    help = "Solr management commands"
    args = "--delete-all --update-all --default-shards"
    
    option_list = BaseCommand.option_list + (
        make_option("--delete-all", action='store_true', dest="delete_all", help="Deletes all Courses stored in Solr"),
        make_option("--update-all", action="store_true", dest="update_all", help="Updates Solr with current version of Courses"),
        make_option("--default-shards", action="store_true", dest="solr_default_shards", help="Generates config line for defaults/solconfig.xml"),
    )
    
    def handle(self, *args, **options):
        if options.get('update_all'):
            self.update_all()
        if options.get('delete_all'):
            self.delete_all()
        if options.get('solr_default_shards'):
            self.solr_default_shards()

    def solr_default_shards(self):
        languages = sorted(set(LANG_MAPPING.values()))
        solr_url = settings.SOLR_URL.lstrip('http://')
        line = '<str name="shards">' + ','.join([solr_url % lang for lang in languages]) + '</str>'
        self.stdout.write(line)

    def delete_all(self):
        self.stdout.write("Deleting all Courses in Solr")
    
        for lang in sorted(set(LANG_MAPPING.values())):            
            SOLR_URL = settings.SOLR_URL % lang
            solr = pysolarized.Solr(SOLR_URL)

            self.stdout.write("Deleting %s at %s" % (lang, SOLR_URL)) 

            solr.deleteAll()
            solr.commit()

    def update_all(self):
        self.stdout.write("Updating all Courses in Solr")

        c = 0
        for lang in sorted(set(LANG_MAPPING.values())):
            SOLR_URL = settings.SOLR_URL % lang
            solr = pysolarized.Solr(SOLR_URL)

            self.stdout.write("Adding %s to %s" % (lang, SOLR_URL))

            for course in Course.objects.filter(language__iexact=lang):
                if not course.title: continue

                solr_doc = {
                    'id': course.linkhash,
                    'title': course.title,
                    'description': course.description,
                    'link': course.linkurl,
                    'source': course.provider.name,
                    'language': course.language,
                    'is_member': True
                }
                solr.add(solr_doc)

                if c % 200 == 0:
                    solr.commit()
                c+=1
            solr.commit()
            solr.optimize()
