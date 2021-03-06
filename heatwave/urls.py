from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'heatwave.views.home', name='home'),
    # url(r'^heatwave/', include('heatwave.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    
    (r'^map/$', 'core.views.map_view'),
    (r'^alert/(?P<alert_id>\d+)/$', 'core.views.clear_alert'),
)
