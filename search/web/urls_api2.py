from django.conf.urls import patterns, url
from .views import api2

urlpatterns = patterns('',
	url(r'^sources/$', api2.SourceList.as_view(), name='sources'),
    url(r'^sources/(?P<pk>\d+)/$', api2.SourceDetail.as_view(), name='source-detail'),
    url(r'^sources/(?P<source_id>\d+)/courses/$',
            api2.SourceCourseList.as_view(), name='source-course-list'),
    url(r'^sources/(?P<source_id>\d+)/courses/(?P<pk>\d+)/$',
            api2.CourseDetail.as_view(), name='course-detail'),
	url(r'^$', api2.index, name='api2-root'),
)
