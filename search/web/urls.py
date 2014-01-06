from django.conf.urls import patterns, include, url
from . import views

urlpatterns = patterns('',
	url(r'^providers/(?P<provider>\d+)/courses/$', views.ProviderCourseList.as_view(), name='provider-courses-list'),
	url(r'^providers/(?P<pk>\d+)/$', views.ProviderDetail.as_view(), name='provider-detail'),
	url(r'^providers/$', views.ProviderList.as_view(), name='providers-list'),

	url(r'^courses/stats/$', 'web.views.course_stats', name='course-stats'),	
	url(r'^courses/latest/$', views.CourseLatestList.as_view(), name='course-latest'),
	url(r'^courses/view/(?P<linkhash>\w+)/$', views.CourseDetail.as_view(lookup_field='linkhash'), name='course-detail'),
	url(r'^courses/search/$', 'web.views.search', name='search-query'),

	url(r'^languages/(?P<language>[\w|\W]+)/courses/$', views.CourseList.as_view(lookup_field='language'), name='language-courses-list'),
	url(r'^languages/$', views.LanguageList.as_view({'get': 'list'}), name='language-list'),

	url(r'^categories/(?P<category>[\w|\W]+)/(?P<language>[\w|\W]+)/$', views.CourseCategoryList.as_view(), name='category-course-list'),
	url(r'^categories/(?P<category>[\w|\W]+)/$', views.CourseCategoryList.as_view(), name='category-course-list'),
	
	
	url(r'^categories/(?P<language>[\w|\W]+)/$', views.CategoryList.as_view(), name='category-list'),
	url(r'^categories/$', views.CategoryList.as_view(), name='category-list'),
)	