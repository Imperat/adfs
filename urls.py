from django.conf.urls.defaults import patterns, include, url
from views import *
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'adfs.views.home', name='home'),
    # url(r'^adfs/', include('adfs.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
        url(r'^admin/', include(admin.site.urls)),
        url(r'main/$', hello),
        url(r'stat/$', stat),
        url(r'bombardiers/$', boms),
        url(r'calend/$', calend),
)
