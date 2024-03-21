from django.shortcuts import render, redirect

from .models import *
from .forms import CommentsForm

def index(request):
    comment = Comments.objects.all()
    error = ''
    if request.method == "POST":
        form = CommentsForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.name_id = request.user.id
            form.save()
            return redirect('home')
        else:
            error = 'Форма неверна!'

    form = CommentsForm()
    context = {
        'form': form,
        'error': error,
        "comment":comment
    }

    return render(request, 'main/index.html', context)

def catalog(request):
    products = Product.objects.all()
    return render(request, 'main/catalog.html', {"products":products})