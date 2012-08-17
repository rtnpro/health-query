from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import logout as _logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.conf import settings
from social_auth.signals import socialauth_registered
from healthquery.userspace.forms import UserProfileForm
from googlemaps import GoogleMaps
from healthquery.userspace.forms import *


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


@login_required
def user_dashboard(request):
    return render_to_response("userspace/dashboard.html",
        context_instance=RequestContext(request))


@login_required
def user_settings_profile(request):
    try:
        profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist, e:
        profile = UserProfile(user=request.user)
    if request.method == "POST":
        profile_form = UserProfileForm(request.POST, instance=profile)
        if profile_form.is_valid():
            profile = profile_form.save(commit=False)
            address = profile.get_address()
            gmaps = GoogleMaps()
            lat, lng = gmaps.address_to_latlng(address)
            profile.geometry = 'POINT({lng} {lat})'.format(lng=lng, lat=lat)
            profile.save()
            return HttpResponseRedirect(reverse("user_settings_profile"))
    else:
        profile_form = UserProfileForm(instance=profile)
    return render_to_response("userspace/settings_profile.html",
        {'form': profile_form, 'profile': profile},
        context_instance=RequestContext(request))