from django.conf.urls import patterns, include, url

urlpatterns = patterns('web.views',
	url(r'^course/view/(?P<linkhash>\w+)/$', 'course_detail'),
	url(r'search/', 'index', name='search_query')
)