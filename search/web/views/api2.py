# -*- coding: utf-8 -*-
from collections import OrderedDict

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework import generics
# from rest_framework.permissions import IsAuthenticated

from data.models import Source, Course, MerlotCategory
from ..serializers import SourceSerializer, CourseRetrieveUpdateSerializer, \
    CategoryListSerializerAPI2, CategoryFlatListSerializer

@api_view(['GET'])
def index(request):
    """
    This is v2 Open Data API to Courses that are currently tracked by OpenCourseWare Consortium.

    It's currently under active development.
    """
    return Response(OrderedDict([
        ('sources', reverse('api2:sources', request=request)),
        ('source-detail', reverse('api2:source-detail', args=('15',), request=request)),
        ('source-course-list', reverse('api2:source-course-list', args=('15',), request=request)),
        ('course-detail', reverse('api2:course-detail', args=('26',), request=request)),
        ('category-list', reverse('api2:category-list', request=request))
    ]))


class SourceList(generics.ListAPIView):
    # permission_classes = (IsAuthenticated,)
    serializer_class = SourceSerializer
    paginate_by = 200
    queryset = Source.objects.filter(provider__active=True)

    def get_queryset(self):
        return Source.objects.filter(provider__active=True, **self.kwargs) \
                .order_by('provider__name')


class SourceDetail(generics.RetrieveAPIView):
    # permission_classes = (IsAuthenticated,)
    serializer_class = SourceSerializer
    queryset = Source.objects.filter(provider__active=True)


class SourceCourseList(generics.ListAPIView):
    # permission_classes = (IsAuthenticated,)
    serializer_class = CourseRetrieveUpdateSerializer

    def get_queryset(self, *args, **kwargs):
        return Course.objects.filter(provider__active=True,
                                     source__pk=self.kwargs.get('source_id'))


class CourseDetail(generics.RetrieveUpdateAPIView):
    # permission_classes = (IsAuthenticated,)
    serializer_class = CourseRetrieveUpdateSerializer

    def get_queryset(self, *args, **kwargs):
        return Course.objects.filter(provider__active=True)

class CategoryList(generics.ListAPIView):
    """ Primary difference form API V1, is that now id's that we return are equal to our internal
    objects and `category_id` is renamed to `merlot_id` to make it clearer, that it's an external
    identifier"""

    serializer_class = CategoryListSerializerAPI2
    model = MerlotCategory
    paginate_by = 2000

    def get_queryset(self):
        qs = MerlotCategory.objects.filter(parent=None)

        return MerlotCategory.objects.add_related_count(qs, Course, 'merlot_categories', 'o_count', True)

    def serialize_tree(self, queryset, depth=0, max_depth=-1):
        depth += 1
        for obj in queryset:
            data = CategoryListSerializerAPI2(obj).data
            if depth < max_depth:
                children = MerlotCategory.objects.add_related_count(obj.children.all(), Course, 'merlot_categories', 'o_count', True )
                data['children'] = self.serialize_tree(children, depth=depth, max_depth=max_depth)
            yield data

    def list(self, request, **kwargs):
        data = self.serialize_tree(self.get_queryset(), max_depth=5)
        return Response(data)

class FlatCategoryList(generics.ListAPIView):
    serializer_class = CategoryFlatListSerializer
    model = MerlotCategory
    paginate_by = 2000
    ordering = ('name',)

    def get_queryset(self):
        return MerlotCategory.objects.all()
