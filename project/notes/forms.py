from django import forms

from .models import Note
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Button, ButtonHolder, Field
class CreateNoteModelForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = [
            'header',
            'text',
            'status'
        ]

    header = forms.CharField(required=True)
    text = forms.CharField(required=True)
    status = forms.BooleanField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-inline'
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Field('header'),
            Field('text'),
            Field('status'),
            ButtonHolder(Submit('order', 'Order', css_class='btn btn-danger'))
        )