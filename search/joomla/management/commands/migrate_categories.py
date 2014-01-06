# -*- coding: utf-8 -*-
from optparse import make_option
from pprint import pprint
import hashlib
import requests

from django.core.management.base import BaseCommand

from data.models import Course, Category, Provider
from joomla.models import JosOcwOntology, JosOcwCourseOntology, JosOcwCatalogCourses

class Command(BaseCommand):
    help = "Migrates categories from joomla to our django model"

    def handle(self, *args, **options):
        # remove Student circle, it doesn't belong in our database
        Provider.objects.filter(pk=21).delete()
        # remove dead feeds
        JosOcwCatalogCourses.objects.filter(source__in=['Students Circle Network','Novell, Inc.', 'Universidade de Santiago de Compostela', 'Weber State University',
                                                      'Keio University']).delete()
        JosOcwCatalogCourses.objects.filter(pk__in=[5411,]).delete()

        # calculate hashes for oce course catalogs so it's in sync with out main database
        # for course in JosOcwCatalogCourses.objects.all():
        #   digest = hashlib.md5(course.linkurl.encode('utf-8')).hexdigest()
        #   if digest != course.linkhash:
        #       print 'new digest for', [course.title]
        #       course.linkhash = digest
        #       course.save()

        for ontology in JosOcwOntology.objects.filter(parent_id=0):
            parent_category, is_created = Category.objects.get_or_create(name=ontology.category)

            for course_link in JosOcwCourseOntology.objects.filter(category=ontology):
                try:
                    course = Course.objects.get(linkhash=course_link.course.linkhash)
                    course.categories.add(parent_category)
                    print 'added', parent_category, [course.title]
                except Course.DoesNotExist:
                    pass

                # print [course_link.course.linkhash, course_link.course.title, course_link.course.id]

            for ontology_child in ontology.josocwontology_set.all():
                child_category, is_created = Category.objects.get_or_create(name=ontology_child.category, parent=parent_category)
                for course_link in JosOcwCourseOntology.objects.filter(category=ontology_child):
                    # print [course_link.course.linkhash, course_link.course.title, course_link.course.id]
                    try:
                        course = Course.objects.get(linkhash=course_link.course.linkhash)
                        course.categories.add(child_category)
                        print 'added', child_category, [course.title]
                    except Course.DoesNotExist:
                        pass
