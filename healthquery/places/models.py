from django.db import models
from django_google_maps import fields as map_fields


class Place(models.Model):
    CHOICES = (
        ('HP', 'Hospital'),
        ('PH', 'Pharmacy'),
        ('NH', 'Nursing Home'),
        ('PC', 'Private Chamber')
    )
    place_type = models.CharField(max_length="2", choices=CHOICES)
    address = map_fields.AddressField(max_length=200)
    geolocation = map_fields.GeoLocationField(max_length=100)
