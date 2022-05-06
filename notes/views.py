from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, UpdateView

from .forms import CreateNoteForm, SelectNotesToDeleteForm, UpdateNoteForm
from .models import Note

class IndexPage(ListView):
    template_name = 'index.html'
    paginate_by = 4
    model = Note
    context_object_name = 'notes'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_note_form'] = CreateNoteForm
        context['select_notes_form'] = SelectNotesToDeleteForm
        context['complited'] = Note.objects.filter(status=True)
        context['selected'] = Note.objects.filter(delete_status=True)
        return context

    def post(self, request, *args, **kwargs):
        create_note_form = CreateNoteForm(request.POST or None)
        select_notes_form = SelectNotesToDeleteForm(request.POST or None)
        if create_note_form.is_valid():
            create_note_form.save()
            return redirect('index_page')
        if select_notes_form.is_valid():
            print(select_notes_form.cleaned_data)
            notes_to_delete = select_notes_form.cleaned_data.get('choices')
            notes_to_delete.delete()
            return redirect('index_page')

class DeleteNote(DeleteView):
    model = Note
    success_url = reverse_lazy('index_page')
    template_name = 'confirm_delete_note.html'

class DeleteComplited(ListView):
    queryset = Note.objects.filter(status = True)
    template_name = 'confirm_delete_completed.html'
    success_url = reverse_lazy('index_page')

    def get(self, request, *args, **kwargs):
        queryset = Note.objects.filter(status=True)
        return render(request, self.template_name, {'notes': queryset})
    def post(self, request, *args, **kwargs):
        queryset = Note.objects.filter(status=True).delete()
        return redirect(self.success_url)

class UpdateNote(UpdateView):
    model = Note
    form_class = UpdateNoteForm
    template_name = 'update_note.html'
    success_url = reverse_lazy('index_page')

# ПЕРЕПИСАТЬ НА КЛАСС
def change_status(request, pk):
    note = Note.objects.get(id=pk)
    note.change_status()
    note.save()
    return redirect('/')

def change_delete_status(request, pk):
    note = Note.objects.get(id=pk)
    note.change_delete_status()
    note.save()
    return redirect('/')

class DeleteSelected(ListView):
    queryset = Note.objects.filter(delete_status = True)
    template_name = 'confirm_delete_completed.html'
    success_url = reverse_lazy('index_page')

    def get(self, request, *args, **kwargs):
        queryset = Note.objects.filter(delete_status=True)
        return render(request, self.template_name, {'notes': queryset})
    def post(self, request, *args, **kwargs):
        queryset = Note.objects.filter(delete_status=True).delete()
        return redirect(self.success_url)