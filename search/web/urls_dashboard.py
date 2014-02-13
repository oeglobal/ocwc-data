from django.conf.urls import patterns, include, url

from .views import dashboard

urlpatterns = patterns('',
	url(r'^source/(?P<pk>\d+)/course/list/$', dashboard.SourceCourseListView.as_view(), name='source-course-list'),
	url(r'^course/(?P<linkhash>\w+)/$', dashboard.CourseDetailView.as_view(lookup_field='linkhash'), name='course-view'),

	url(r'^source/(?P<edit_key>\w+)/add/$', dashboard.CourseAddView.as_view(), name='course-add'),
)