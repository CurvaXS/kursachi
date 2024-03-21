from django.shortcuts import render

from .models import *

def index(request):
    return render(request, 'main/index.html')

def catalog(request):
    prod = Product.objects.order_by('-id')
    return render(request, 'main/catalog.html', {"prod":prod})