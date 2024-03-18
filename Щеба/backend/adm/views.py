from django.shortcuts import render, get_object_or_404, redirect

from django.views.generic import DetailView
from django.views.generic.base import View 

from .models import Note, Comment

from .forms import CommentForm

def home(request):
    nt = Note.objects.all()
    return render(request, 'main/index.html', {'note':nt})


class Post_detail(DetailView):
    model = Note
    slug_field = 'url'
    template_name = 'main/note_detail.html'


class AddComm(View):

    def post(self, request, pk):
        form = CommentForm(request.POST)
        note = Note.objects.get(id=pk)
        if form.is_valid():
            form.save(commit=False)
            form.note = note
            form.save()
        return redirect('/')