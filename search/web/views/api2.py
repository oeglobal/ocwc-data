# -*- coding: utf-8 -*-
from collections import OrderedDict

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework import generics

from data.models import Source
from ..serializers import SourceSerializer

@api_view(['GET'])
def index(request):
    """
    This is v2 Open Data API to Courses that are currently tracked by OpenCourseWare Consortium.

    It's currently under active development.
    """
    return Response(OrderedDict([
        ('sources', reverse('api2:sources', request=request)),
        ('source-detail', reverse('api2:source-detail', args=('15',), request=request)),
    ]))

class SourceList(generics.ListAPIView):
    serializer_class = SourceSerializer
    paginate_by = 200
    queryset = Source.objects.filter(provider__active=True)

    def get_queryset(self):
        return Source.objects.filter(provider__active=True, **self.kwargs) \
                .order_by('provider__name')

class SourceDetail(generics.RetrieveAPIView):
    serializer_class = SourceSerializer
    queryset = Source.objects.filter(provider__active=True)
