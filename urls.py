from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.conf import settings
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', '_tea.views.home', name='home'),
    # url(r'^_tea/', include('_tea.foo.urls')),
    url(r'^$', '_tea.blog.views.index'), 
    url(r'^entry/(\d+)/$', '_tea.blog.views.entry'), 
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}), 

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
