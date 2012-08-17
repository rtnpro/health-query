from django import forms
from django.core.urlresolvers import reverse

from crispy_forms.helper import FormHelper
from crispy_forms.layout import (Layout, Div, Submit, HTML,
     Button, Row, Field, Column)
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions
from healthquery.userspace.models import UserProfile

class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        exclude = ('user', 'geometry',)

    def __init__(self, *args, **kwargs):
        helper = FormHelper()
        helper.form_id = "userprofile-form"
        helper.form_class = 'form-vertical'
        helper.form_action = reverse("user_settings_profile")
        helper.form_method = "POST"
        helper.form_show_errors = True
        helper.layout = Layout(
            Field('address_line1', css_class='input-xxlarge dual'),
            Field('address_line2', css_class='input-xxlarge dual'),
            Div(
                Div(
                    Field('zipcode', css_clas="input-large"),
                    css_class="span3"
                ),
                Div(
                    Field('locality', css_class='input-large'),
                    css_class="span3"
                ),
                css_class="row"
            ),
            Div(
                Div(
                    Field('state', css_class='input-large'),
                    css_class="span3"
                ),
                Div(
                    Field('country', css_clas="input-large"),
                    css_class="span3"
                ),
                css_class="row"
            ),
            Submit('submit', "Save changes", css_class="btn-primary btn-large")
        )
        self.helper = helper
        super(UserProfileForm, self).__init__(*args, **kwargs)