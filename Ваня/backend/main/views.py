from django.shortcuts import render

from .models import *

def index(request):
    return render(request, 'main/index.html')

def catalog(request):
    products = Product.objects.all()
    return render(request, 'main/catalog.html', {"products":products})