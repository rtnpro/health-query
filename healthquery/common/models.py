from django.contrib.gis.db import models
from django.contrib.auth.models import User as User
from django.utils.translation import ugettext_lazy as _
from address.models import AddressField


class BaseAddressModel(models.Model):
    #address
    address = AddressField(blank=True, null=True)

    # geolocation
    geometry = models.PointField(srid=4326)
    geomanager = models.GeoManager()

    class Meta:
        abstract = True


class UserProfile(BaseAddressModel):
    user = models.OneToOneField(User, verbose_name=_('user'),
            related_name='profile')

