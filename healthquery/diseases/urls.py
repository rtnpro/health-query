from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^diseases/add/$',
        'healthquery.diseases.views.disease_add',
        name='disease_add'
    ),
    url(r'^diseases/d/(?P<disease_id>\d+)/$',
        'healthquery.diseases.views.disease_detail',
        name="disease_detail"
    ),
    url(r'^remedies/r/(?P<remedy_id>\d+)/ajax/$',
        'healthquery.diseases.views.ajax_get_remedy_details',
        name="ajax_get_remedy_details"
    ),
    url(r'^medicines/m/(?P<medicine_id>\d+)/ajax/$',
        'healthquery.diseases.views.ajax_get_medicine_details',
        name="ajax_get_medicine_details"
    )
)
