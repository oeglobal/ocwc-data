from django.conf.urls import patterns, include, url

from .views import dashboard

urlpatterns = patterns('',
	url(r'^source/(?P<pk>\d+)/course/list/$', dashboard.SourceCourseListView.as_view(), name='source-course-list'),
)