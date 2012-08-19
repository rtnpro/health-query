from django.db import models
from django.utils.translation import ugettext_lazy as _
from django_google_maps import fields as map_fields
from healthquery.common.models import BaseAddressModel


class Place(BaseAddressModel):
    CHOICES = (
        ('HP', 'Hospital'),
        ('PH', 'Pharmacy'),
        ('NH', 'Nursing Home'),
        ('PC', 'Private Chamber')
    )
    name = models.CharField(verbose_name=_("name"), max_length=100)
    place_type = models.CharField(max_length="2", choices=CHOICES)

    class Meta:
        unique_together = ('name', 'place_type', 'zipcode', 'state', 'country')
