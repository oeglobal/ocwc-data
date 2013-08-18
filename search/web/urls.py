from django.conf.urls import patterns, include, url
from . import views

urlpatterns = patterns('',
	url(r'^courses/latest/', 'web.views.course_latest', name='course-latest'),
	url(r'^courses/view/(?P<linkhash>\w+)/$', views.CourseDetail.as_view(), name='course-detail'),
	url(r'^search/', 'web.views.search', name='search-query'),
)

# urlpatterns += patterns('',
# 	url(r'^', include('rest_framework_swagger.urls')),
# )