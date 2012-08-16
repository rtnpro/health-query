from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from haystack.views import SearchView, search_view_factory
from haystack.query import SearchQuerySet
from healthquery.common.forms import HealthQuerySearchForm
from healthquery.diseases.models import Disease

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

sqs = SearchQuerySet().models(Disease)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'healthquery.views.home', name='home'),
    # url(r'^healthquery/', include('healthquery.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'healthquery.views.home'),
    url(r'^diseases/', include('healthquery.diseases.urls')),
    url('^markdown/', include( 'django_markdown.urls')),
    url(r'^search/$', search_view_factory(
        view_class=SearchView,
        template="search/search.html",
        searchqueryset=sqs,
        form_class=HealthQuerySearchForm
    ), name="health_query_search"),
    url(r'^search/', include('haystack.urls')),
    url(r'^accounts/logout/$', 'healthquery.common.views.logout',
        name='logout'),
    url(r'^accounts/login/$', 'healthquery.common.views.login',
        name='login'),
    url(r'', include('social_auth.urls')),
    url(r'^support/$', 'healthquery.common.views.support',
        name='support'),
)

urlpatterns += staticfiles_urlpatterns()
