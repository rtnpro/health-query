from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = patterns('',
    url(
        r'^home/$',
        'healthquery.userspace.views.user_dashboard',
        name='user_dashboard'
    ),
    url(
        r'^accounts/logout/$',
        'healthquery.userspace.views.logout',
        name='logout'
    ),
    url(
        r'^accounts/login/$',
        'healthquery.userspace.views.login',
        name='login'
    ),
    url(
        r'^accounts/settings/profile/$',
        'healthquery.userspace.views.user_settings_profile',
        name='user_settings_profile'
    ),
)