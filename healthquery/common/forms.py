from django import forms
from django.core.urlresolvers import reverse
from haystack.forms import HighlightedSearchForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field, Column
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions


class HealthQuerySearchForm(HighlightedSearchForm):
    def __init__(self, *args, **kwargs):
        super(HealthQuerySearchForm, self).__init__(*args, **kwargs)
        self.fields['q'].widget.attrs['class'] = 'span6 textInput'
        self.fields['q'].widget.attrs['style'] = 'height:35px;'
        self.fields['q'].widget.attrs['placeholder'] = 'How do you feel?'
        self.fields['q'].label = ''