from django import forms

from .models import Note
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Button, ButtonHolder, Field


class CreateNoteForm(forms.ModelForm):
    class Meta:
        model = Note
        exclude = ('user',)
        fields = [
            'header',
            'text',
            'status',
        ]
        labels = {
            'header': 'Заголовок',
            'text': 'Описание',
            'status': 'Статус',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-inline'
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Field('header', css_class='w-50', label='Заголовок'),
            Field('text', css_class='w-50'),
            Field('status'),
            ButtonHolder(Submit('добавить', 'Добавить', css_class='btn btn-success'))
        )


class UpdateNoteForm(forms.ModelForm):
    class Meta:
        model = Note
        exclude = ('user',)
        fields = [
            'header',
            'text',
            'status',
        ]
        labels = {
            'header': 'Заголовок',
            'text': 'Описание',
            'status': 'Статус',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-inline'
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Field('header', css_class='w-50'),
            Field('text', css_class='w-50'),
            Field('status'),
            ButtonHolder(Submit('изменить', 'Изменить',
                         css_class='btn btn-warning'))
        )


class SelectNotesToDeleteForm(forms.Form):
    choices = forms.ModelMultipleChoiceField(
        queryset = Note.objects.all(),  # this is optional
        widget = forms.CheckboxSelectMultiple,
        label = ''
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-inline'
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Field('choices', css_class='w-50'),
            ButtonHolder(Submit('изменить', 'Изменить',
                         css_class='btn btn-warning'))
        )
