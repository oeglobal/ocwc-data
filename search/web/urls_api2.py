from django.conf.urls import patterns, url
from .views import api2

urlpatterns = patterns('',
	url(r'^sources/$', api2.SourceList.as_view(), name='sources'),
    url(r'^sources/(?P<pk>\d+)/$', api2.SourceDetail.as_view(), name='source-detail'),
	url(r'^$', api2.index, name='api2-root'),
)
