from django.conf import settings
from django.shortcuts import render_to_response
from django.template import RequestContext


def login(request):
    request.session['next'] = request.GET.get('next',
            settings.LOGIN_REDIRECT_URL)
    return HttpResponseRedirect(reverse('socialauth_begin',
        args=['google-oauth2'])
    )


@login_required
def logout(request):
    redirect_to = request.GET.get('next', settings.LOGOUT_REDIRECT_URL)
    _logout(request)
    return HttpResponseRedirect(redirect_to)


def support(request):
    """Render support page for health query"""
    return render_to_response('support.html',
        {'forum_name': settings.SUPPORT_FORUM_NAME},
        context_instance=RequestContext(request)
    )