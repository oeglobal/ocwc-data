# -*- coding: utf-8 -*-
import pysolarized
from pprint import pprint 
import json
from requests import ConnectionError

from django.shortcuts import render
from django.http import HttpResponse, Http404

from django.conf import settings

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.views import APIView
from rest_framework import viewsets, generics, mixins

from .serializers import *
from data.models import Course, Provider

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
    [search]: http://www.ocwconsortium.org/en/courses/search
    [github]: https://github.com/ocwc/ocwc-data
    [dbdump]: http://data.ocwconsortium.org/dbdump/
    """

    return Response({
        'search': reverse('search-query', request=request),
        'course-stats': reverse('course-stats', request=request),
        'course-latest': reverse('course-latest', request=request),
        'course-detail': reverse('course-detail', args=('3ab55059096d526167866d058a550818',), request=request),
        'providers-list': reverse('providers-list', request=request),
        'provider-detail': reverse('provider-detail', args=('1'), request=request),
        'provider-course-list': reverse('provider-courses-list', args=('1'), request=request),
        'language-list': reverse('language-list', request=request),
        'language-courses-list': reverse('language-courses-list', kwargs={'language': 'English'}, request=request)
    })

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
    Retrieve information on a specific course. Currently through linkhash parameter.
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
        return Course.objects.filter(**self.kwargs)
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

class LanguageCourseList(generics.ListAPIView):
    """
    List all available Courses for Language
    """
    def get_queryset(self):
        return Course.objects.filter(**self.kwargs)
    serializer_class = CourseListSerializer
    paginate_by = 25
    paginate_by_param = 'limit'