from django.views.generic import ListView,DetailView
from django.shortcuts import redirect, render
from .models import *
from multiprocessing import context
from django.http import HttpResponse,JsonResponse
import json



# Create your views here.
# def index(request):
#     product = Product.objects.all()
#     customer = Customer.objects.all()
#     return render (request,'store/main.html',{'products':list(product),'customers':list(customer)})


class Homeview(ListView):
    model = Product
    template_name = 'store/index.html'


# product details
def product_details(request,product_id):
    product = Product.objects.get(id = product_id )
    return render(request,'store/product_details.html',{'product':product})



# cart function
def cart(request):
    # check if user is authenticated
    if request.user.is_authenticated:
        customer = request.user.customer
        # get an order if exists or create an order
        order,created =  Order.objects.get_or_create(customer=customer)
        # get items attached to the order
        # query child object order item
        items = order.orderitem_set.all()
        # count order items
        count = order.orderitem_set.all().count()
    # if user is not authenticated
    else:
        items = []
        order = {'get_cart_total':0,'get_cart_items':0}
    
    context = {'items':items,'order':order,'count':count}
    return render(request,'store/cart.html',context)

# checkout function
def checkout(request):
      # check if user is authenticated
    if request.user.is_authenticated:
        customer = request.user.customer
        # get an order if exists or create an order
        order,created =  Order.objects.get_or_create(customer=customer,complete = False)
        # get items attached to the order
        # query child object order item
        items = order.orderitem_set.all()
        # count order items
        count = order.orderitem_set.all().count()
    # if user is not authenticated
    else:
        items = []
        order = {'get_cart_total':0,'get_cart_items':0}
    
    context = {'items':items,'order':order,'count':count}
    return render(request,'store/checkout.html',context)

# update item view
def updateItem(request):
    # get data from the backend
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('action:',action)
    print('product:',productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order,created = Order.objects.get_or_create(customer=customer,complete=False)

    orderItem,created = OrderItem.objects.get_or_create(order=order,product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <=0:
        orderItem.delete()

    return JsonResponse('Item was added',safe=False)




# reduce inventory
def reduce_inventory(request,pk):
    product = Product.objects.get(id=pk)
    form = Updateinventory(request.POST)
    # form = Product(request.POST['inventory'])

    if request.method == 'POST':
        if form.is_valid():
            quantity = int(request.POST['inventory'])
            product.inventory -= quantity
            product.save()
            return redirect('home' )

    return render (request,'store/reduce_inventory.html',{'form': form})



