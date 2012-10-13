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
    formatted_address = models.CharField()
    formatted_phone_number = models.CharField()
    international_phone_number = models.CharField()
    vicinity = models.CharField()
    icon = models.URLField()
    types = models.CharField()
    url = models.URLField()
    website = models.URLField()

    # ranking to be synced with Google places
    rating = models.FloatField(verbose_name='rating', help_text='Google'
        ' Places rating.')
    google_places_refid = models.CharField(verbose_name=u'google places '
        'reference id', help_text='Reference id for this place in '
        'Google places.')
    google_places_id = models.CharField()

    class Meta:
        unique_together = ('name', 'place_type', 'zipcode', 'state', 'country')


class Reviews(models.Model):
    author_name = models.CharField(verbose_name=u'Author name',
        help_text='Author name')
    author_url = models.CharField()
    text = models.TextField()
    time = models.DateTimeField()
    aspect_rating = models.FloatField()
    aspect_type = models.CharField()
    place = models.ForeignKey(Place)

    class Meta:
        verbose_name = _('Reviews')

        verbose_name_plural = _('Reviewss')


    def __unicode__(self):
        pass


class Event(models.Model):
    event_id = models.CharField()
    start_time = models.DateTimeField()
    summary = models.TextField()
    url = models.URLField()
    
    class Meta:
        verbose_name = _('Event')

        verbose_name_plural = _('Events')


    def __unicode__(self):
        pass
    
            
