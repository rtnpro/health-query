from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from healthquery.places.models import Place


class SpecializationManager(models.ModelManager):
    def get_by_name_or_alias(self, name):
        if name is None:
            raise Specialization.DoesNotExist("No specialization matched "
                "this query.")
        specialization = cache.get('specialization:name_or_alias:%s' % name,
            None)
        if specialization is None:
            try:
                specialization = Specialization.objects.get(
                    Q(name=name) | Q(aliases__contains='%s,' % name))
            except Specialization.DoesNotExist, e:
                pass
        return specialization

    def for_disease(self, disease):
        return self.filter(diseases=disease)


class Specialization(models.Model):
    name = models.CharField(verbose_name=u'name', help_text='Specialization'
        ' of a doctor.')
    aliases = models.CharField(verbose_name=u'aliases', help_text='A comma '
        'separated aliases for a specialization')
    diseases = models.ManyToManyField(Disease, verbose_name=u'diseases',
        help_text='Diseases that this specialization can handle.')

    objects = SpecializationManager()

    class Meta:
        verbose_name = _('Specialization')

        verbose_name_plural = _('Specializations')


    def __unicode__(self):
        pass
            

class DoctorManager(models.ModelManager):

    def for_disease(self, disease):
        return self.filter(
            specialization__in=Specialization.objects.for_disease(disease))

    def with_specialization(self, specialization):
        return self.filter(specialization=specialization)


class Doctor(models.Model):
    user = models.OneToOneField(User, blank=True, null=True)
    registration_id = models.CharField(max_length=20)
    places = models.ManyToManyField(Place, through="DoctorLocation",
            blank=True, null=True)
    specialization = models.ManyToManyField(Specialization)

    objects = DoctorManager()


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
