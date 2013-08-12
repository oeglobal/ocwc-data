import pysolarized
from pprint import pprint 
import json
from requests import ConnectionError

from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import CourseSerializer
from joomla.models import JosOcwCourses

def index(request):
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
def course_detail(request, linkhash):
    """
    Retrieve course instance.
    """              
    try:
    	course = JosOcwCourses.objects.get(linkhash=linkhash)
    except JosOcwCourses.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CourseSerializer(course)
        return Response(serializer.data)
