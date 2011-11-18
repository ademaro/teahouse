# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url

from django.contrib import admin
from django.conf import settings
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', '_tea.views.home', name='home'),
    # url(r'^_tea/', include('_tea.foo.urls')),
    url(r'^$', 'blog.views.index'),
    url(r'^entry/(\d+)/$', '_tea.blog.views.entry'), 
    url(r'^tags/(\d+)/$', '_tea.blog.views.tags'), 
    #url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/var/www/z-gu.ru/_tea/static'}),
    #url(r'mu-a0e9c771-fb62bfcb-31460fd2-f2daa98a.txt', 'django.views.static.serve', {'document_root': '/var/www/z-gu.ru/_tea/static'}),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
)
