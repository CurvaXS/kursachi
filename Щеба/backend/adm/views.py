from django.shortcuts import render, get_object_or_404

from django.views.generic import DetailView

from .models import Note, Comment

def home(request):
    nt = Note.objects.all()
    return render(request, 'main/index.html', {'note':nt})


def post_detail(request, id):
    post = get_object_or_404(Note, id=id)
    data = {
        'photo_url': post.photo_url,
        'date': post.date,
        'name': post.name
    }
    return render(request, 'main/detail.html', {'post':data})

def post_comments(request, id,):
    comm = Comment.objects.all()
    return render(request, 'main/detail.html', {'comm': comm})

class Post_detail(DetailView):
    model = Note
    slug_field = 'url'
    template_name = 'main/note_detail.html'