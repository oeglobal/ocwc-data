# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand

from optparse import make_option
from pprint import pprint
import json

from data.models import Course, Provider, Source

class Command(BaseCommand):
    help = """
        Imports VLN database dump
        $ bin/django vln_female_speakers --lectures-file dumps/lectures.json  --authors-file dumps/authors.json --edges-file dumps/edges.json
    """
    args = "--lectures-file --authors-file"

    option_list = BaseCommand.option_list + (
        make_option("--lectures-file", action="store", dest="lectures-file", help="Path to lectures.json"),
        make_option("--authors-file", action="store", dest="authors-file", help="Path to authors.json"),
        make_option("--edges-file", action="store", dest="edges-file", help="Path to edges.json")
    )


    def handle(self, *args, **options):
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
                            author_edge = authors.get(author_id)
                            author_names.append(author_edge.get('name'))

                            if author_edge.get('gender') == 'F':
                                print author_edge.get('name').encode('utf-8'), '\t', title.encode('utf-8'), '\t', url
                                break

                        
                        author = ', '.join(author_names)

                    else:
                        author = ''