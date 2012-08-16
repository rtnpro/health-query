from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import logout as _logout
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.conf import settings
from social_auth.signals import socialauth_registered


def login(request):
    request.session['next'] = request.GET.get('next',
            settings.LOGIN_REDIRECT_URL)
    return HttpResponseRedirect(reverse('socialauth_begin',
        args=['google-oauth2'])
    )


def logout(request):
    redirect_to = request.GET.get('next', settings.LOGOUT_REDIRECT_URL)
    _logout(request)
    return HttpResponseRedirect(redirect_to)


def support(request):
    return render_to_response('support.html',
        {'forum_name': settings.SUPPORT_FORUM_NAME},
        context_instance=RequestContext(request)
    )
