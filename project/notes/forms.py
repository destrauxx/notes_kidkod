from django import forms

from .models import Note
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Button, ButtonHolder, Field

class CreateNoteForm(forms.Form):
    header = forms.CharField(required=True, label='Заголовок')
    text = forms.CharField(required=True, widget=forms.Textarea(), label='Описание')
    status = forms.BooleanField(label='Статус')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-inline'
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Field('header', css_class='w-50'),
            Field('text', css_class='w-50'),
            Field('status'),
            ButtonHolder(Submit('добавить', 'Добавить', css_class='btn btn-success'))
        )