from django.db import models
from django.contrib.auth.models import User as _User
from django.utils.translation import ugettext_lazy as _
from django_google_maps import fields as map_fields


class User(_User):
	address = map_fields.AddressField(max_length=200)
	geolocation = map_fields.GeoLocationField(max_length=100)