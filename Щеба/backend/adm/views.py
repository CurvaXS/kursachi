from django.shortcuts import render, get_object_or_404

from .models import Note

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