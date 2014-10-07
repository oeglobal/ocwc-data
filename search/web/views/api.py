# -*- coding: utf-8 -*-
import json
import pysolarized
from pprint import pprint 
from collections import OrderedDict

from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.conf import settings

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.views import APIView
from rest_framework import viewsets, generics, mixins

from ..serializers import *
from data.models import Course, Provider, Category

@api_view(['GET'])
def index(request):
    """
    This is experimental Open Data API to Courses that are currently tracked by OpenCourseWare Consortium.

    We are currently setting first version of API endpoints as we transition to this system. Please note that
    API endpoints and/or return values might change at any time. We plan to finalize first version by the end of 2013.

    This API currently directly powers [OCWC course search][search].

    If you have any questions or comments please contact [Jure Cuhalev][jure].

    You can follow development in our [Github repository][github].

    If you would just like a copy of the data, you can download Excel export [from here][dbdump].

    [jure]: mailto:jure@ocwconsortium.org
    [search]: http://www.oeconsortium.org/courses/
    [github]: https://github.com/ocwc/ocwc-data
    [dbdump]: http://data.ocwconsortium.org/dbdump/
    """

    return Response(OrderedDict([
        ('search', reverse('api:search-query', request=request)),
        ('course-stats', reverse('api:course-stats', request=request)),
        ('course-latest', reverse('api:course-latest', request=request)),
        ('course-detail', reverse('api:course-detail', args=('59069fd6f629c3eefa5f8c5d6a39d96a',), request=request)),
        ('providers-list', reverse('api:providers-list', request=request)),
        ('provider-detail', reverse('api:provider-detail', args=('1'), request=request)),
        ('provider-course-list', reverse('api:provider-courses-list', args=('1'), request=request)),
        
        ('language-list', reverse('api:language-list', request=request)),
        ('language-courses-list', reverse('api:language-courses-list', kwargs={'language': 'English'}, request=request)),

        ('category-course-list', reverse('api:category-course-list', kwargs={'category': 'Computer Science'}, request=request)),
        # ('category-language-course-list', reverse('category-course-list', kwargs={'language': 'English', 'category': 'Computer Science'}, request=request)),

        ('category-list-default', reverse('api:category-list', request=request)),
        ('category-list', reverse('api:category-list', kwargs={'language': 'English'}, request=request))
    ]))

def search(request):
    if request.GET.get('q'):
        q = request.GET.get('q')
        SOLR_URL = settings.SOLR_URL % 'default'
        solr = pysolarized.Solr(SOLR_URL)

        results = solr.query(q)
        if results:
            response = results.documents
        else:
            response = {'error': 'Search is currently not available'}
    else:
        response = {'error': 'Please use q parameter for search'}

    return HttpResponse(json.dumps(response), content_type="application/json")

@api_view(['GET'])
def course_stats(request):
    return Response({
        'courses': Course.objects.all().count(),
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
    queryset = Course.objects.all().order_by('-id')[:10]
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
        data = Course.objects.all().order_by('language').values_list('language', flat=True).distinct()
        return Response(data)

class CourseList(generics.ListAPIView):
    """
    List all available Courses for Language
    """
    def get_queryset(self):
        return Course.objects.filter(**self.kwargs)
    serializer_class = CourseListSerializer
    paginate_by = 25
    paginate_by_param = 'limit'

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
        
        lookup_params = {}
        if category:
            lookup_params['categories__name'] = category
        if language:
            lookup_params['language'] = language

        return Course.objects.filter(**lookup_params)

class CategoryList(generics.ListAPIView):
    """
    List all available Categories for Courses. By default it shows all languages,
    but supports filtering by language.
    """    
    model = Category

    def serialize_tree(self, queryset, language=None):
        for obj in queryset:
            data = CategoryListSerializer(obj, language=language).data
            data['children'] = self.serialize_tree(obj.children.all(), language=language)
            yield data

    def list(self, request, **kwargs):
        queryset = self.get_queryset().filter(parent=None)
        data = self.serialize_tree(queryset, language=kwargs.get('language'))
        return Response(data)