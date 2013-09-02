# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand

from optparse import make_option
from pprint import pprint
import json

from data.models import Course, Provider, Source

class Command(BaseCommand):
    help = """
        Imports VLN database dump
        $ bin/django import_vln --lectures-file dumps/lectures.json  --authors-file dumps/authors.json --edges-file dumps/edges.json
    """
    args = "--lectures-file --authors-file"

    option_list = BaseCommand.option_list + (
        make_option("--lectures-file", action="store", dest="lectures-file", help="Path to lectures.json"),
        make_option("--authors-file", action="store", dest="authors-file", help="Path to authors.json"),
        make_option("--edges-file", action="store", dest="edges-file", help="Path to edges.json")
    )


    def handle(self, *args, **options):

        provider, created = Provider.objects.get_or_create(
                                name = "VideoLectures.net",
                                external_id = "18281",
                                active = True
                            )

        source, created = Source.objects.get_or_create(
                                provider = provider,
                                defaults = {
                                    'kind': 'manual',
                                }
        )

        if options.get('lectures-file') and options.get('authors-file') and options.get('edges-file'):
            authors = json.loads(open(options.get('authors-file')).read())
            lectures = json.loads(open(options.get('lectures-file')).read())
            edges = json.loads(open(options.get('edges-file')).read())

            for edge_id in edges:
                lecture = lectures.get(edge_id)

                if lecture and lecture.get('enabled') and lecture.get('public'):
                    lec_type = lecture.get('type')
                    if ('event' in lec_type) or ('curriculum' in lec_type) or ('external' in lec_type) or ('referenced course' in lec_type) or ('advertisment' in lec_type): 
                        continue

                    url = "http://videolectures.net/%s/" % lecture.get('url')
                    title = lecture.get('text').get('title')
                    description = lecture.get('text').get('desc', '')

                    if not title:
                        continue

                    edge = edges.get(edge_id)
                    
                    if edge.get("authors"):
                        authors_list = edge.get("authors").keys()
                        author_names = []

                        for author_id in authors_list:
                            author_names.append(authors.get(author_id).get('name'))
                        
                        author = ', '.join(author_names)
                    else:
                        author = ''

                    lang = lecture.get('lang')
                    if   lang == 'en': language = 'English'
                    elif lang == 'sl': language = 'Slovenian'
                    elif lang == 'de': language = 'German'
                    elif lang == 'es': language = 'Spanish'
                    elif lang == 'it': language = 'Italian'
                    elif lang == 'fr': language = 'French'
                    elif lang == 'hr': language = 'Croatian'
                    elif lang == 'nl': language = 'Dutch'
                    elif lang == 'pl': language = 'Polish'
                    elif lang == 'ru': language = 'Russian'
                    elif lang == 'sr': language = 'Serbian'
                    elif lang == 'uk': language = 'Ukrainian'
                    else:
                        raise Exception("Unknown language: " + lang)

                    course, created = Course.objects.get_or_create(
                                        provider = provider,
                                        source = source,
                                        linkurl = url,
                                        defaults = {
                                            'title': title,
                                            'description': description,
                                            'author': author,
                                            'language': language
                                        }
                    )