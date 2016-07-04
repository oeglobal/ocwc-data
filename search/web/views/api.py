# -*- coding: utf-8 -*-
import json
import datetime
from collections import OrderedDict

from urllib import urlencode
from urlparse import urlsplit

from lxml import etree
import xml.etree.ElementTree as ET

import pysolarized
import requests
import requests_cache

from django.conf import settings
from django.http import HttpResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework import viewsets, generics

from ..serializers import *
from data.models import Course, Source, Provider, MerlotCategory, MerlotLanguage
from data.management.commands.merlot import MERLOT_LANGUAGE_SHORT

@api_view(['GET'])
def index(request):
    """
    This is v1 Open Data API to Courses that are currently tracked by OpenCourseWare Consortium. It is stable as of beginning 2015. We won't remove properties, but we might add additional ones.

    This API currently directly powers [OCWC course search][search].

    There is also a [v2 of API][v2], where we're trying to make API conform to [JSON API schema][jsonapi]

    If you have any questions or comments please contact [Jure Cuhalev][jure].

    You can follow development in our [Github repository][github].

    If you would just like a copy of the data, you can download Excel export [from here][dbdump].

    [jure]: mailto:jure@ocwconsortium.org
    [search]: http://www.oeconsortium.org/courses/
    [github]: https://github.com/ocwc/ocwc-data
    [dbdump]: http://data.ocwconsortium.org/dbdump/
    [jsonapi]: http://jsonapi.org/
    [v2]: /api/v2/
    """

    return Response(OrderedDict([
        ('search', reverse('api:search-query', request=request)),
        ('course-stats', reverse('api:course-stats', request=request)),
        ('course-latest', reverse('api:course-latest', request=request)),
        ('course-detail', reverse('api:course-detail', args=('5fa03a5c8db7311b6c3e3235dc616ae0',), request=request)),
        ('providers-list', reverse('api:providers-list', request=request)),
        ('provider-detail', reverse('api:provider-detail', args=('1'), request=request)),
        ('provider-course-list', reverse('api:provider-courses-list', args=('1'), request=request)),

        ('language-list', reverse('api:language-list', request=request)),
        ('language-courses-list', reverse('api:language-courses-list', kwargs={'language': 'English'}, request=request)),

        ('category-course-list', reverse('api:category-course-list', kwargs={'category': '372822'}, request=request)),
        # ('category-language-course-list', reverse('category-course-list', kwargs={'language': 'English', 'category': 'Computer Science'}, request=request)),

        ('category-list-default', reverse('api:category-list', request=request)),
        # ('category-list', reverse('api:category-list', kwargs={'language': 'English'}, request=request))
    ]))

def search(request):

    def _build_course_doc(course):
        if course.source:
            source = course.source.provider.name
        elif course.author_organization:
            source = course.author_organization
        elif not course.author and course.author_organization:
            source = course.author_organization
        elif course.author:
            source = course.author
        else:
            source = ''

        provider_id = ''
        if course.source:
            provider_id = course.source.provider.id

        cat_tree = []
        for cat in course.merlot_categories.all():
            cat_tree.append('/'.join( ['All'] + map( unicode, cat.get_ancestors() ) + [cat.name] ) )

        if course.merlot_languages.exists():
            language = ','.join([lang.name for lang in course.merlot_languages.all()])
        else:
            language = course.language

        doc = {
            'description': course.description,
            'language': language,
            'title': course.title,
            'is_member': bool(course.provider),
            'source': source,
            'link': course.linkurl,
            'id': course.linkhash,
            'author': course.author or '',
            'author_organization': course.author_organization,
            'oec_provider_id': provider_id,
            'categories': cat_tree,
            'merlot_id': course.merlot_id
        }

        return doc

    def encode_obj(in_obj):
        """ http://stackoverflow.com/a/26568590/141200 """

        def encode_list(in_list):
            out_list = []
            for el in in_list:
                out_list.append(encode_obj(el))
            return out_list

        def encode_dict(in_dict):
            out_dict = {}
            for k, v in in_dict.iteritems():
                out_dict[k] = encode_obj(v)
            return out_dict

        if isinstance(in_obj, unicode):
            return in_obj.encode('utf-8')
        elif isinstance(in_obj, list):
            return encode_list(in_obj)
        elif isinstance(in_obj, tuple):
            return tuple(encode_list(in_obj))
        elif isinstance(in_obj, dict):
            return encode_dict(in_obj)

        return in_obj

    def _update_metadata(material):
        url = material.find('URL').text
        try:
            course = Course.objects.get(linkhash=Course.calculate_linkhash(url))

            if course.merlot_synced:
                return course

        except Course.DoesNotExist:
            course = Course()

        try:
            photo_url = material.find('photoURL').text
        except AttributeError:
            photo_url = ''

        course_data = {
            'linkurl': url,
            'title': material.find('title').text,
            'merlot_id': material.find('materialid').text,
            'description': material.find('description').text,
            'author': material.find('authorName').text or '',
            'author_organization': material.find('authorOrg').text or '',
            'image_url': photo_url,
            'merlot_xml': ET.tostring(material, encoding='utf-8'),
            'merlot_synced_date': datetime.datetime.now(),
            'merlot_synced': True,
        }

        course_data['creative_commons_commercial'] = 'Unsure'
        creativecommons = material.find('creativecommons').text
        if 'cc-' in creativecommons:
            course_data['creative_commons'] = 'Yes'

            if 'nc' in creativecommons:
                course_data['creative_commons_commercial'] = 'No'

            if 'sa' in creativecommons:
                course_data['creative_commons_derivatives'] = 'Sa'
            elif 'nd' in creativecommons:
                course_data['creative_commons_derivatives'] = 'No'
            else:
                course_data['creative_commons_derivatives'] = 'Yes'
        else:
            creativecommons = 'No'

        # course_data['language'] = language

        course_domain = urlsplit(url).netloc
        if Source.objects.filter(url__icontains=course_domain).exists():
            source = Source.objects.filter(url__icontains=course_domain)[0]

            course.source = source
            course.provider = source.provider

        for k, v in course_data.items():
            setattr(course, k, v)
        course.save()

        # course.merlot_categories.clear()
        for category in material.find('categories').findall('category'):
            category_id = category.attrib.get('href').split('=')[1]
            course.merlot_categories.add(MerlotCategory.objects.get(merlot_id=category_id))

        for language_short in material.find('languages').findall('language'):
            if language_short.text not in MERLOT_LANGUAGE_SHORT:
                continue

            language = MERLOT_LANGUAGE_SHORT[language_short.text]

            merlot_language, is_created = MerlotLanguage.objects.get_or_create(name=language)
            # print merlot_language
            course.merlot_languages.add(merlot_language)

        course.save()

        return course

    def _merlot_search(params):
        if settings.DEBUG:
            requests_cache.install_cache('merlot')

        parser = etree.XMLParser(recover=True)

        r = requests.get(settings.MERLOT_API_URL + '/materialsAdvanced.rest', params=params)
        tree = ET.fromstring(r.content, parser=parser)

        try:
            num_results = int(tree.find('nummaterialstotal').text)
        except AttributeError:
            num_results = 0


        documents = []
        if num_results > 0:
            for material in tree.findall('material'):
                course = _update_metadata(material)

                doc = _build_course_doc(course)
                documents.append(doc)

        return documents, num_results


    """Use `q` paramater to specify query string, `legacy=1` to use the old search"""

    if request.GET.get('q') and request.GET.get('legacy', '0') != '0':
        q = request.GET.get('q')
        SOLR_URL = settings.SOLR_URL % 'default'
        solr = pysolarized.Solr(SOLR_URL)

        solr_kwargs = {'start': 0, 'rows': 10}
        page = int(request.GET.get('page', 1))

        if page:
            solr_kwargs['start'] = (page - 1) * 10

        results = solr.query(q, **solr_kwargs)
        if results:

            documents = []
            for solr_doc in results.documents:
                course = Course.objects.get(linkhash=solr_doc['id'])
                doc = _build_course_doc(course)

                documents.append(doc)

            response = {
                'page': page,
                'count': results.results_count,
                'documents': documents
            }

            if results.results_count > page * 10:
                response['next_page'] = urlencode(encode_obj({'page': page+1, 'legacy': 'on', 'q': q}))

            if page > 1:
                response['previous_page'] = urlencode(encode_obj({'page': page-1, 'legacy': 'on', 'q': q}))

        else:
            response = {'error': 'Search is currently not available'}

    elif request.GET.get('q'):
        page = int(request.GET.get('page', 1))
        q = request.GET.get('q')

        params = {
            'licenseKey': settings.MERLOT_KEY,
            'page': page,
            'keywords': q,
            'creativeCommons': 1,
            'sort.property': 'overallRating',
            'materialType': ['Online Course', 'Open Textbook']
        }
        data, count = _merlot_search(params)

        response = {
            'page': page,
            'count': count,
            'documents': data
        }

        if count > page * 10:
            response['next_page'] = urlencode(encode_obj({'page': page+1, 'q': q}))

        if page > 1:
            response['previous_page'] = urlencode(encode_obj({'page': page-1, 'q': q}))

    else:
        response = {'error': 'Please use q parameter for search'}

    return HttpResponse(json.dumps(response), content_type="application/json")

# class SearchResults(generics.ListAPIView):
#     """Use `q` paramater to specify query string. Pagination is not supported."""
#     serializer_class = CourseSeachResultsSerializer

#     def get_queryset(self):
#         query = self.request.GET.get('q', '').lower()

#         SearchQuery.objects.get_or_create(
#             query = query,
#             defaults = {
#                 'language': ''
#             }
#         )

#         queryset = Course.objects.filter(
#                                     Q(title__icontains=query) | \
#                                     Q(description__icontains=query) | \
#                                     Q(author__icontains=query) | \
#                                     Q(author_organization__icontains=query)
#                                     )[:20]

#         return queryset


@api_view(['GET'])
def course_stats(request):
    return Response({
        'courses': Course.objects.all().count(),
        'courses_ocw': Course.objects.filter(provider__isnull=False).count(),
        'providers': Provider.objects.all().count()
        })

class CourseDetail(generics.RetrieveAPIView):
    """
    Retrieve information on a specific course. Course identifier is MD5 hash of
    course URL. It's not optimal, but I haven't found anything better. This means
    that as courses get moved around it will change.

    In python you can generate it by running:

        import hashlib
        link_url = 'http://ocw.uci.edu/lectures/lecture.aspx?id=406'
        hashlib.md5(link_url.encode('utf-8')).hexdigest()
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CourseLatestList(generics.ListAPIView):
    """
    List latest Courses added to the database.
    """
    queryset = Course.objects.all().exclude(provider__isnull=True).order_by('-id')[:10]
    serializer_class = CourseSerializer

class ProviderDetail(generics.RetrieveAPIView):
    """
    Retrieve specific information about each provider. Providers are usually educational institutions
    from which we aggregate course data.
    """
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer

class ProviderCourseList(generics.ListAPIView):
    """
    List all available Courses for Provider
    """
    def get_queryset(self):
        return Course.objects.filter(**self.kwargs).order_by('title')
    serializer_class = CourseListSerializer
    paginate_by = 25
    paginate_by_param = 'limit'

class ProviderList(generics.ListAPIView):
    """
    List all Course Providers in database
    """
    queryset = Provider.objects.all().order_by('name')
    serializer_class = ProviderSerializer

class LanguageList(viewsets.ViewSet):
    """
    List all Languages in the database
    """
    def list(self, request):
        data = MerlotLanguage.objects.all().order_by('name').values_list('name', flat=True).distinct()
        return Response(data)

class CourseList(generics.ListAPIView):
    """
    List all available Courses for Language
    """
    serializer_class = CourseListSerializer
    paginate_by = 25
    paginate_by_param = 'limit'

    def get_queryset(self):
        return Course.objects.filter(source__isnull=False, source__disabled=False, **self.kwargs)

    def list(self, request, *args, **kwargs):
        response = super(CourseList, self).list(request, args, kwargs)

        response.data['language'] = self.kwargs.get('language')

        return response

class CourseCategoryList(generics.ListAPIView):
    """
    List all available Courses by Language and Category
    """
    serializer_class = CourseListSerializer
    paginate_by = 25
    paginate_by_param = 'limit'

    def get_queryset(self):
        category = self.kwargs.pop('category', None)
        language = self.kwargs.pop('language', None)

        lookup_params = {'source__isnull': False, 'source__disabled': False}
        if category:
            try:
                self.category = MerlotCategory.objects.get(merlot_id=category)
                category_ids = [self.category.id] + \
                                list(MerlotCategory.objects.get(merlot_id=category) \
                                .get_children() \
                                .values_list('id', flat=True))

                lookup_params['merlot_categories__in'] = category_ids
            except MerlotCategory.DoesNotExist:
                return Course.objects.none()

            except ValueError:
                pass

        if language:
            lookup_params['merlot_languages__name'] = language

        return Course.objects.filter(**lookup_params)

    def list(self, request, *args, **kwargs):
        response = super(CourseCategoryList, self).list(request, args, kwargs)

        if hasattr(self, 'category'):
            response.data['title'] = self.category.name

        return response


class CategoryList(generics.ListAPIView):
    """
    List all available Categories for Courses.
    """
    model = MerlotCategory

    def get_queryset(self):
        qs = MerlotCategory.objects.filter(parent=None)

        return MerlotCategory.objects.add_related_count(qs, Course, 'merlot_categories', 'o_count', True)

    def serialize_tree(self, queryset, language=None, depth=0, max_depth=-1):
        depth += 1
        for obj in queryset:
            data = CategoryListSerializer(obj, language=language).data
            if depth < max_depth:
                children = MerlotCategory.objects.add_related_count(obj.children.all().exclude(course__source__isnull=False), Course, 'merlot_categories', 'o_count', True )
                data['children'] = self.serialize_tree(children, language=language, depth=depth, max_depth=max_depth)
            yield data

    def list(self, request, **kwargs):
        data = self.serialize_tree(self.get_queryset(), language=kwargs.get('language'), max_depth=2)
        return Response(data)
