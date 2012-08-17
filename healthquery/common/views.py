from django.conf import settings
from django.shortcuts import render_to_response
from django.template import RequestContext


def support(request):
    """Render support page for health query"""
    return render_to_response('support.html',
        {'forum_name': settings.SUPPORT_FORUM_NAME},
        context_instance=RequestContext(request)
    )