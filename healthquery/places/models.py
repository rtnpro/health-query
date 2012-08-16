from django.db import models
from django_google_maps import fields as map_fields
from healthquery.common.models import BaseAddressModel


class Place(BaseAddressModel):
    CHOICES = (
        ('HP', 'Hospital'),
        ('PH', 'Pharmacy'),
        ('NH', 'Nursing Home'),
        ('PC', 'Private Chamber')
    )
    place_type = models.CharField(max_length="2", choices=CHOICES)
