from django.db import models
from django.utils.translation import ugettext_lazy as _
import tagging
from tagging.fields import TagField


class Remedy(models.Model):
    name = models.CharField(max_length=200, verbose_name=_('Name'),
            help_text=_("Name for this remedy"))
    description = models.TextField(max_length=5000, verbose_name=_(
        "Description"), default=None, blank=True, null=True,
        help_text=_("Description for this remedy."))
    tags = TagField(default=None, blank=True, null=True,
            verbose_name=_("Tags"))

    class Meta:
        unique_together = ('name',)

    def __unicode__(self):
        return self.name


tagging.register(Remedy, tag_descriptor_attr='tagsobj')


class Medicine(models.Model):
    name = models.CharField(max_length=200, verbose_name=_('Chemical name'),
            help_text=_("Chemical name for this medicine"))
    description = models.TextField(max_length=5000, verbose_name=_(
        "Description"), blank=True, default=None, null=True,
        help_text=_("Description for this medicine."))
    tags = TagField(default=None, blank=True, null=True,
            verbose_name=_("Tags"))

    class Meta:
        unique_together=('name',)

    def __unicode__(self):
        return self.name

tagging.register(Medicine, tag_descriptor_attr='tagsobj')


class Disease(models.Model):
    name = models.CharField(max_length=200, verbose_name=_('Name'),
            help_text=_('Name for this disease'))
    summary = models.TextField(max_length=200, verbose_name=_('Summary'),
            help_text=_('Summary for this disease'), default=None, blank=True)
    description = models.TextField(max_length=1000, default=None, blank=True,
            verbose_name=_('Description'), help_text=_('Description for this '
                'disease'))
    SEVERITY_CHOICES = (
        (0, _('Low')),
        (1, _('Normal')),
        (2, _('High')),
        (3, _('Critical')),
    )
    severity = models.PositiveIntegerField(default=0,
            verbose_name=_("Severity"), choices=SEVERITY_CHOICES,
            help_text=_("Severity for this disease."))
    medicines = models.ManyToManyField(Medicine, default=None, blank=True,
            verbose_name=_('Medicines'), help_text=_(
                "Medicines for this disease"))
    remedies = models.ManyToManyField(Remedy, default=None, blank=True,
            verbose_name=_("Remedies"), help_text=_(
                "Remedies for this disease"))
    tags = TagField(default=None, blank=True, null=True,
            verbose_name=_("Tags"))

    class Meta:
        unique_together=('name',)

    def __unicode__(self):
        return self.name

tagging.register(Disease, tag_descriptor_attr='tagsobj')
