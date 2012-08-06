from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^add/$',
        'healthquery.diseases.views.disease_add',
        name='disease_add'
    ),
    url(r'^d/(?P<disease_id>\d+)/$',
        'healthquery.diseases.views.disease_detail',
        name="disease_detail"
    )
)
