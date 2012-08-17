from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from healthquery.common.models import BaseAddressModel


class UserProfile(BaseAddressModel):
    user = models.OneToOneField(User, verbose_name=_('user'),
            related_name='profile')

    @property
    def first_name(self):
        return self.user.first_name

    @property
    def last_name(self):
        return self.user.last_name

    @property
    def name(self):
        user = self.user
        return (user.first_name + ' ' + user.last_name) or user.username

    @property
    def username(self):
        return self.user.username

    @property
    def email(self):
        return self.user.email

    def get_address(self):
        address = "{locality}, {state} {zipcode}, {country}".format(
            locality=self.locality, state=self.state,
            zipcode=self.zipcode, country=self.country)
        return address

    def __unicode__(self):
        return self.username