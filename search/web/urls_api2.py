from django.conf.urls import patterns, url
from .views import api2

urlpatterns = patterns('',
	url(r'^friends/$', api2.index, name='api-root'),
	url(r'^$', api2.index, name='api-root'),
)