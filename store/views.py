from django.shortcuts import render
from .models import Product,Customer
from multiprocessing import context
from django.http import HttpResponse


# Create your views here.
def index(request):
    product = Product.objects.all()
    customer = Customer.objects.all()
    return render (request,'store/main.html',{'products':list(product),'customers':list(customer)})
