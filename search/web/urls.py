from django.conf.urls import patterns, include, url
from . import views

urlpatterns = patterns('',
	url(r'^providers/', views.ProviderList.as_view(), name='providers-list'),
	url(r'^courses/latest/', views.CourseLatestList.as_view(), name='course-latest'),
	url(r'^courses/view/(?P<linkhash>\w+)/$', views.CourseDetail.as_view(), name='course-detail'),
	url(r'^search/', 'web.views.search', name='search-query'),
)