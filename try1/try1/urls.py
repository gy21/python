from django.conf.urls import patterns, include, url

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # this will look up the signups app for the views.py file and tries to find a home view
    url(r'^$', 'signups.views.home', name='home'),
    # url(r'^try1/', include('try1.try1.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
 
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
