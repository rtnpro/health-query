from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from healthquery.places.models import Place


class Doctor(models.Model):
    user = models.OneToOneField(User, blank=True, null=True)
    registration_id = models.CharField(max_length=20)
    places = models.ManyToManyField(Place, through="DoctorLocation",
            blank=True, null=True)


class DoctorLocation(models.Model):
    doctor = models.ForeignKey(Doctor)
    place = models.ForeignKey(Place)


class Day(models.Model):
    DAYS = (
        ('MON', 'Monday'),
        ('TUE', 'Tuesday'),
        ('WED', 'Wednesday'),
        ('THU', 'Thursday'),
        ('FRI', 'Friday'),
        ('SAT', 'Saturday'),
        ('SUN', 'Sunday')
    )
    name = models.CharField(max_length=3, choices=DAYS)


class Timing(models.Model):
    doctor_location = models.ForeignKey(DoctorLocation)
    available_from = models.TimeField()
    available_to = models.TimeField()
    days = models.ManyToManyField(Day)
