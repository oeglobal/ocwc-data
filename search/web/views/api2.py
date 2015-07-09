# -*- coding: utf-8 -*-
from collections import OrderedDict

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics

from data.models import Source
from ..serializers import SourceListSerializer

@api_view(['GET'])
def index(request):
    """
    This is v2 Open Data API to Courses that are currently tracked by OpenCourseWare Consortium.

    It's currently under active development.
    """
    return Response(OrderedDict([]))

class SourceList(generics.ListAPIView):
    serializer_class = SourceListSerializer
    paginate_by = 25

    def get_queryset(self):
        return Source.objects.filter(provider__active=True, **self.kwargs)
