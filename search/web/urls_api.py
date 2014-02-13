from django.conf.urls import patterns, include, url
from .views import api

urlpatterns = patterns('',
	url(r'^providers/(?P<provider>\d+)/courses/$', api.ProviderCourseList.as_view(), name='provider-courses-list'),
	url(r'^providers/(?P<pk>\d+)/$', api.ProviderDetail.as_view(), name='provider-detail'),
	url(r'^providers/$', api.ProviderList.as_view(), name='providers-list'),

	url(r'^courses/stats/$', 'web.views.api.course_stats', name='course-stats'),	
	url(r'^courses/latest/$', api.CourseLatestList.as_view(), name='course-latest'),
	url(r'^courses/view/(?P<linkhash>\w+)/$', api.CourseDetail.as_view(lookup_field='linkhash'), name='course-detail'),
	url(r'^courses/search/$', 'web.views.api.search', name='search-query'),

	url(r'^languages/(?P<language>[\w|\W]+)/courses/$', api.CourseList.as_view(lookup_field='language'), name='language-courses-list'),
	url(r'^languages/$', api.LanguageList.as_view({'get': 'list'}), name='language-list'),

	# url(r'^categories/(?P<category>[\w|\W]+)/(?P<language>[\w|\W]+)/$', views.CourseCategoryList.as_view(), name='category-course-list'),
	url(r'^categories/(?P<category>[\w|\W]+)/$', api.CourseCategoryList.as_view(), name='category-course-list'),
	
	
	url(r'^categories/(?P<language>[\w|\W]+)/$', api.CategoryList.as_view(), name='category-list'),
	url(r'^categories/$', api.CategoryList.as_view(), name='category-list'),
)	