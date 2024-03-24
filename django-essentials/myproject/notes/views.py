from typing import Any
from django.shortcuts import render, redirect
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView

from .models import Notes
from .forms import NotesForm

# Create your views here.


class NotesCreateView(CreateView):
    model = Notes
    # fields = ['title', 'content']
    success_url = '/smart/notes'
    template_name = 'notes/notes_create.html'
    form_class = NotesForm


class NotesListView(ListView):
    model = Notes
    context_object_name = 'notes'
    template_name = 'notes/notes_list.html'
    ordering = ['-created']
    paginate_by = 10


# def list(request):
#     all_notes = Notes.objects.all()
#     return render(request, 'notes/notes_list.html', {'notes': all_notes})


class NotesDetailView(DetailView):
    model = Notes
    context_object_name = 'note'
    template_name = 'notes/notes_detail.html'

    def get_object(self, queryset=None):
        try:
            return super().get_object(queryset)
        except Http404:
            # return render(self.request, '404.html', {})
            # return HttpResponseRedirect(reverse('notes-detail-list', args=[1]))
            # return HttpResponseRedirect(reverse('notes-list'))
            return "404 - Sorry, the requested note does not exist!"


# def detail(request, pk):
#     try:
#         note = Notes.objects.get(pk=pk)
#     except Notes.DoesNotExist:
#         raise Http404("Note does not exist")
#     return render(request, 'notes/notes_detail.html', {'note': note})
