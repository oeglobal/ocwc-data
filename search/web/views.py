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
from rest_framework import viewsets, generics

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

    [jure]: mailto:jure@ocwconsortium.org
    [search]: http://www.ocwconsortium.org/en/courses/search
    """

    return Response({
        'search': reverse('search-query', request=request),
        'course-latest': reverse('course-latest', request=request),
        'course-detail': reverse('course-detail', args=('3ab55059096d526167866d058a550818',), request=request),
        'providers-list': reverse('providers-list', request=request),
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

class CourseDetail(APIView):
    """
    Retrieve information on a specific course. Currently through linkhash parameter.
    """
    def get_object(self, linkhash):
        try:
            return Course.objects.get(linkhash=linkhash)
        except Course.DoesNotExist:
            raise Http404

    def get(self, request, linkhash, format=None):
        course = self.get_object(linkhash)
        serializer = CourseSerializer(course, many=False)
        return Response(serializer.data)

class CourseLatestList(generics.ListAPIView):
    """
    List latest Courses added to the database.
    """
    queryset = Course.objects.all().order_by('-id')[:10]
    serializer_class = CourseSerializer

class ProviderList(generics.ListAPIView):
    """
    List all Course Providers in database
    """
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer