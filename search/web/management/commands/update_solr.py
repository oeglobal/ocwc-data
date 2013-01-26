# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
import argparse

from web.models import *
from joomla.models import *

from web.solr import SolrInterface
import cld

SOLR_URL = "http://localhost:8984/solr/%s/"

LANG_MAPPING = {
    'English': 'english',
        'en':   'english',
        'en-GB': 'english',
        'en-gb': 'english',
        'en-US': 'english',
        'en-us': 'english',
        u'ingl\xe9s': u'english',
    'Catalan': 'catalan',
        'ca': 'catalan',
    'Chamorro': 'chamorro',
    'Chinese': 'chinese',
        'Chineset': 'chinese',
        'Chinese - Traditional': 'chinese',
    'Dutch': 'dutch',
    'French': 'french',
    'Spanish': 'spanish',
        'es': 'spanish',
        'es-ES': 'spanish',
        u'espa\xf1ol': u'spanish',
    'Hebrew': 'hebrew',
        'he': 'hebrew',
    'Indonesian': 'indonesian',
    'Japanese': 'japanese',
        'ja': 'japanese',
    'Persian': 'persian',
        'fa-IR': 'persian',
    'Polish': 'polish',
    'Portuguese': 'portuguese',
    'Russian': 'russian',
        'ru-ru': 'russian',
    'Galician': 'galician',
    'German': 'german',
    'Korean': 'korean',
    'Malay': 'malay',
}

def clear_solr():
    c = 0
    for lang in LANG_MAPPING:
        solr_lang = LANG_MAPPING[lang]
        print "deleting solr:", solr_lang

        SOLR_ENDPOINTS  = { solr_lang: SOLR_URL % solr_lang }
        SOLR_DEFAULT_ENDPOINT = solr_lang
        solr = SolrInterface(SOLR_ENDPOINTS, SOLR_DEFAULT_ENDPOINT)

        solr.deleteAll()
        solr.commit()

def make_lang():
    print "languages"
    lang_all = []
    for c in JosOcwCourses.objects.order_by('language').all():
      if c.language not in LANG_MAPPING: 
        lang_all.append(c.language)
        print [c.language]

    extra_docs = {}

    # sanitize languages
    for lang in LANG_MAPPING:
        solr_lang = LANG_MAPPING[lang]
        # print solr_lang
        for doc in JosOcwCourses.objects.filter(language=lang, enabled=True):
            if solr_lang in ['english',]: 
                topLanguageName, topLanguageCode, isReliable, textBytesFound, details = cld.detect(doc.title.encode('utf-8') + " " + doc.description.encode('utf-8'))
                if topLanguageCode not in  ['en','un']:
                    # force unidentified languages into English
                    if topLanguageCode == 'un':
                        topLanguageName = 'English'

                    doc.language = topLanguageName.lower().capitalize()

                    print topLanguageName, topLanguageCode, isReliable
                    print doc.title, doc.description
                    doc.save()
                    continue

            if doc.language != solr_lang.capitalize():
                print doc.language, '-->', solr_lang.capitalize()
                doc.language = solr_lang.capitalize()
    #             doc.save()

    for doc in JosOcwCourses.objects.all():
        status_id = doc.crmid.civicrmmembership_set.all()[0].status.id
        if status_id not in [2,3,5,7]:
            doc.enabled = 0
            doc.save()

def main():
    # http://fuzzy:8984/solr/english/select?shards=localhost:8984/solr/english/,localhost:8984/solr/catalan/&q=mat*&wt=xml&indent=true&fl=*&rows=100

    c = 0
    for lang in LANG_MAPPING:
        solr_lang = LANG_MAPPING[lang]
        print c, solr_lang

        SOLR_ENDPOINTS  = { solr_lang: SOLR_URL % solr_lang }
        SOLR_DEFAULT_ENDPOINT = solr_lang
        solr = SolrInterface(SOLR_ENDPOINTS, SOLR_DEFAULT_ENDPOINT)

        # print lang
        for doc in JosOcwCourses.objects.filter(language=lang):
            if not doc.title: continue
            
            solr_doc = {
                'id': doc.linkhash,
                'title': doc.title,
                'description': doc.description,
                'link': doc.linkurl,
                'source': doc.source,
                'language': solr_lang.title(),
            }
            solr.add(solr_doc)
            solr.commit()

            if c % 200 == 0:
                print c
                solr.commit()

            c+=1

        solr.commit()
        solr.optimize()


from optparse import make_option

class Command(BaseCommand):
    help = "updates solr with latest documents/courses"

    option_list = BaseCommand.option_list + (
            make_option('--clear', 
                    action='store',
                    dest='clear_solr'),
            make_option('--lang',
                    action='store',
                    dest='make_lang')
        )

    def handle(self, *args, **options):
        if options.get('clear_solr'):
            clear_solr()
        elif options.get('make_lang'):
            make_lang()
        else:
            main()
