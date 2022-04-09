from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, UpdateView

from .forms import CreateNoteForm
from .models import Note

class IndexPage(ListView):
    template_name = 'index.html'
    paginate_by = 4
    
    def get(self, request, *args, **kwargs):
        form = CreateNoteForm()
        return render(request, self.template_name, {'form': form, 'notes': Note.objects.all()})

    def post(self, request, *args, **kwargs):
        form = CreateNoteForm(request.POST or None)
        if form.is_valid():
            header = form.cleaned_data.get('header')
            text = form.cleaned_data.get('text')
            status = form.cleaned_data.get('status')
            new_note = Note.objects.create(header=header, text=text, status=status)
            new_note.save()
            return redirect('index_page')


class CreateNote(CreateView):
    model = Note
    form_class = CreateNoteForm
    template_url = 'create_note_form.html'
    

class DeleteNote(DeleteView):
    model = Note
    success_url = reverse_lazy('index_page')
    template_name = 'confirm_delete_note.html'

# class UpdateNote(UpdateView):

