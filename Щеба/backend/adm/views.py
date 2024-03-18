from django.shortcuts import render, get_object_or_404, redirect

from django.views.generic import DetailView
from django.views.generic.base import View 

from .models import Note, Comment

from .forms import CommentForm

def home(request):
    nt = Note.objects.all()
    return render(request, 'main/index.html', {'note':nt})



def post_detail(request, pk):
    note = get_object_or_404(Note, id=pk)
    comment = Comment.objects.filter(note=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.note.id = note.id
            form.save()
    else:
        form = CommentForm()

    return render(request, 'main/note_detail.html', {
        "note":note,
        "comment": comment,
        "form":form
        })

"""
class Post_detail(DetailView):
    model = Note
    slug_field = 'url'
    template_name = 'main/note_detail.html'


def AddComm(request, pk):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        note = Note.objects.get(id=pk)
        if form.is_valid():
            form.save(commit=False)
            form.note = note
            form.save()
        return redirect('/')
        
    form = CommentForm()
    context = {'form': form}
    return render(request, 'main/note_detail.html', context)
"""
