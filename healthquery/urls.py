from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'healthquery.views.home', name='home'),
    # url(r'^healthquery/', include('healthquery.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'healthquery.views.home'),
    url(r'^diseases/', include('healthquery.diseases.urls')),
    url('^markdown/', include( 'django_markdown.urls')),
)

urlpatterns += staticfiles_urlpatterns()