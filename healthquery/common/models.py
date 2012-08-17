from django.contrib.gis.db import models
from django.contrib.auth.models import User as User
from django.utils.translation import ugettext_lazy as _


class BaseAddressModel(models.Model):
    #address
    address_line1 = models.CharField(verbose_name=_("Address line 1"),
            blank=True, null=True, max_length=255)
    address_line2 = models.CharField(verbose_name=_("Address line 2"),
            blank=True, null=True, max_length=255)
    zipcode = models.CharField(verbose_name=_("Zip code"), max_length=16)
    locality = models.CharField(verbose_name=_("Locality"),
            max_length=255)
    state = models.CharField(verbose_name=("State"), max_length=255)
    country = models.CharField(verbose_name=_("Country"), max_length=255)

    # geolocation
    geometry = models.PointField(srid=4326)
    objects = models.GeoManager()

    class Meta:
        abstract = True