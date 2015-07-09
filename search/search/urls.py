from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'api/v1/', include('web.urls_api', namespace='api')),
    url(r'api/v2/', include('web.urls_api2', namespace='api2')),
    # url(r'dashboard/', include('web.urls_dashboard', namespace='dashboard')),
    url(r'^$', 'web.views.api.index', name='api-root'),
)
