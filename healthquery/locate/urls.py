from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    url('^locate/search/',
        'healthquery.locate.views.search',
        name='locate_search'
    )
)
