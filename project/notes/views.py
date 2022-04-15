from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, UpdateView

from .forms import CreateNoteForm, UpdateNoteForm
from .models import Note

class IndexPage(ListView):
    template_name = 'index.html'
    paginate_by = 4
    model = Note
    context_object_name = 'notes'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CreateNoteForm
        context['complited'] = Note.objects.filter(status=True)
        print(context)
        return context
    # def get(self, request, *args, **kwargs):
    #     form = CreateNoteForm()
    #     complited = Note.objects.filter(status=True)
    #     return render(request, self.template_name, {'form': form, 'notes': Note.objects.all(), 'complited': complited})

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
    
class DeleteNote(DeleteView):
    model = Note
    success_url = reverse_lazy('index_page')
    template_name = 'confirm_delete_note.html'

class UpdateNote(UpdateView):
    model = Note
    form_class = UpdateNoteForm
    template_name = 'update_note.html'
    success_url = reverse_lazy('index_page')

def change_status(request, pk):
    note = Note.objects.get(id=pk)
    note.change_status()
    note.save()
    return redirect('/')

# ПЕРЕПИСАТЬ НА КЛАСС


