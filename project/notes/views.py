from django.shortcuts import render
from django.views.generic import ListView, CreateView

from .forms import CreateNoteModelForm
from .models import Note
# Create your views here.

class IndexPage(ListView):
    template_name = 'index.html'
    queryset = Note.objects.all()

    def get_context_data(self, *kwargs):
        context = super().get_context_data(*kwargs)
        context['form'] = CreateNoteModelForm()

class CreateNote(CreateView):
    model = Note
    form_class = CreateNoteModelForm
    template_url = 'create_note_form.html'

