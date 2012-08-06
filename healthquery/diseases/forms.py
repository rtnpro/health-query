from  django import forms
from django.utils.translation import ugettext as _
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions
from healthquery.diseases.models import Disease

class DiseaseForm(forms.ModelForm):
    class Meta:
        model = Disease

    def __init__(self, *args, **kwargs):
        helper = FormHelper()
        helper.form_class = 'form-vertical'
        helper.form_show_errors = True
        helper.layout = Layout(
            Field('name', css_class='input-xlarge'),
            Field('summary', rows="3", css_class='input-xxlarge'),
            Field('description', rows="10", css_class='input-xxlarge'),
            Field('severity', css_class="chzn-select"),
            Field('remedies', css_class="input-xlarge chzn-select"),
            Field('medicines', css_class="input-xlarge chzn-select"),
            Field('tags', css_class="inpul-xlarge"),
            FormActions(
                Submit('save_changes', 'Save changes', css_class="btn-primary"),
                css_class="",
            )
        )
        self.helper = helper
        super(DiseaseForm, self).__init__(*args, **kwargs)
