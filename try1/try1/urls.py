from django.conf.urls import patterns, include, url

from django.contrib import admin


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'try1.views.home', name='home'),
    # url(r'^try1/', include('try1.try1.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
 
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
