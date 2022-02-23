from django.shortcuts import render
from .models import Product
from multiprocessing import context
from django.http import HttpResponse


# Create your views here.
def index(request):
    product = Product.objects.all()
    return render (request,'index.html',{'products':list(product)})
