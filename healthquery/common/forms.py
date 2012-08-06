from django import forms
from haystack.forms import HighlightedSearchForm

class HealthQuerySearchForm(HighlightedSearchForm):
    def __init__(self, *args, **kwargs):
        super(HealthQuerySearchForm, self).__init__(*args, **kwargs)
        self.fields['q'].widget.attrs['class'] = 'span6 textInput'
        self.fields['q'].widget.attrs['style'] = 'height:35px;'
        self.fields['q'].widget.attrs['placeholder'] = 'How do you feel?'
        self.fields['q'].label = ''
