from ctypes import addressof
from pipes import Template
from django.views.generic import ListView,DetailView,TemplateView,View
from django.shortcuts import redirect, render ,get_object_or_404
from .models import *
from multiprocessing import context
from django.http import HttpResponse,JsonResponse
import json
from django.contrib import messages
from django.utils import timezone
from .forms import CheckoutForm




# Create your views here.
# login
def login(request):
    return render(request,'store/login.html')

# register
def register(request):
    return render(request,'store/register.html')
    
# landing page
class Homeview(ListView):
    model = Product
    template_name = 'store/index.html'

# product details
class ProductDetailView(DetailView):
    model = Product
    template_name = 'store/product_details.html'

# cart function
def cart(request):
    # check if user is authenticated
    if request.user.is_authenticated:
        customer = request.user.customer
        # get an order if exists or create an order
        order,created =  Order.objects.get_or_create(customer=customer,complete=False)
        # get items attached to the order
        items = order.products.all()
    # if user is not authenticated
    else:
        items = []
        order = {'get_cart_total':0,'get_cart_items':0}
    
    context = {'items':items,'order':order}
    return render(request,'store/cart.html',context)


# add products to cart
def add_to_cart(request,slug):
    product = get_object_or_404(Product,slug=slug)
    customer = request.user.customer
    orderitem,created = OrderItem.objects.get_or_create(product=product,customer=customer,complete=False)
    order_qs= Order.objects.filter(customer=customer,complete=False)
    if order_qs.exists():
        order = order_qs[0]
        # check if order item is in order
        if order.products.filter(product__slug=product.slug).exists():
            orderitem.quantity +=1
            orderitem.save()
            messages.success(request,f"{product.title}'s quantity was updated ")
           
        else:
            order.products.add(orderitem)
            order.save()
            messages.success(request,f"{product.title} was added to the cart")
            return redirect("cart")

            
    else:
        placed_at = timezone.now()
        order = Order.objects.create(customer=customer,complete=False,placed_at = placed_at)
        order.products.add(orderitem)
        order.save()
        return redirect("cart")

    return redirect("cart")

# reduce quantity in the cart
def reduce_cart_quantity(request,slug):
    product = get_object_or_404(Product,slug=slug)
    customer = request.user.customer
    order_qs= Order.objects.filter(customer=customer,complete=False)
    if order_qs.exists():
        order = order_qs[0]
        # check if order item is in order
        if order.products.filter(product__slug=product.slug).exists():
            orderitem = OrderItem.objects.filter(product=product,customer=customer,complete=False)[0]
            if orderitem.quantity > 1:
                orderitem.quantity -=1 
                orderitem.save()
                messages.info(request,f"{product.title} quantity was updated")
                
            else:
                order.products.remove(orderitem)
                order.save()
                messages.info(request,f"{product.title} was removed from cart")
            return redirect("cart")

# remove products from cart
def remove_from_cart(request,slug):
    product = get_object_or_404(Product,slug=slug)
    customer = request.user.customer
    order_qs= Order.objects.filter(customer=customer,complete=False)
    if order_qs.exists():
        order = order_qs[0]
        # check if order item is in order
        if order.products.filter(product__slug=product.slug).exists():
            orderitem = OrderItem.objects.filter(product=product,customer=customer,complete=False)[0]
            order.products.remove(orderitem)
            order.save()  
            messages.info(request,f"{product.title} was removed from cart")

        else:
            messages.info(request,f"{product.title} was not in the cart")
            return redirect("cart")
    else:
        # add message
        messages.info(request,"You do not have an active order")
        return redirect("product_details",slug=slug)
    return redirect("cart")



 # checkout class
class CheckoutView(View):
    def get(self, *args, **kwargs):
        customer = self.request.user.customer
        # address = Shippingaddress.objects.get(customer=customer,default=True)
        order = Order.objects.get(customer=customer, complete=False)
        # address = Address.objects.get(user=self.request.user, default=True)
        items = order.products.all()
        form = CheckoutForm()
        context = {
            'form': form,
            'order': order,
            'items':items,
            # 'coupon_form': coupon_form,
            # "DISPLAY_COUPON_FORM": True
            # 'address': address
        }
        return render(self.request, 'store/checkout.html', context)

    def post(self, *args, **kwargs):
        customer = self.request.user.customer
        order,created = Order.objects.get_or_create(customer=customer, complete=False)
        form = CheckoutForm(self.request.POST or None)
        if form.is_valid():
            # print(form.cleaned_data)
            address = form.cleaned_data.get('address')
            street = form.cleaned_data.get('street')
            city = form.cleaned_data.get('city')
            # country = form.cleaned_data.get('country')
            save_info = form.cleaned_data.get('save_info')
            use_default = form.cleaned_data.get('use_default')
            # payment_option = form.cleaned_data.get('payment_option')

            # create an instance of address model and save info
            address = Shippingaddress(
                customer = self.request.user.customer,
                address = address,
                street = street,
                city = city,
                # country = country,
               
            )
            address.save()
            if save_info:
                address.default = True
                address.save()
                
            order.address = address
            order.save()

            # make order complete
            order_items = order.products.all()
            order_items.update(complete=True)
            for item in order_items:
                item.product.inventory -= item.quantity
                item.save()
                item.product.save()
            order.complete = True
            order.save()

            


            
            # if use_default:
            #     address = Shippingaddress.objects.get(
            #         customer = self.request.user.customer, default=True)
            #     order.address = address
            #     order.save()   
            messages.success(self.request, "Your order was successful!") 
            return redirect("cart")
        else:
            print('The form is invalid')

class PaymentView(View):
    def get(self, *args, **kwargs):
        return render(self.request,'store/payments.html')
    























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


















# def index(request):
#     product = Product.objects.all()
#     customer = Customer.objects.all()
#     return render (request,'store/main.html',{'products':list(product),'customers':list(customer)})


# def checkout(request):
#       # check if user is authenticated
#     if request.user.is_authenticated:
#         customer = request.user.customer
#         # get an order if exists or create an order
#         order,created =  Order.objects.get_or_create(customer=customer,complete = False)
#         # get items attached to the order
#         # query child object order item
#         items = order.products.all()

#     # if user is not authenticated
#     else:
#         items = []
#         order = {'get_cart_total':0,'get_cart_items':0}
    
#     context = {'items':items,'order':order}
#     return render(request,'store/checkout.html',context)




# update item view
# def updateItem(request):
#     # get data from the backend
#     data = json.loads(request.body)
#     productId = data['productId']
#     action = data['action']
#     print('action:',action)
#     print('product:',productId)

#     customer = request.user.customer
#     product = Product.objects.get(id=productId)
#     order,created = Order.objects.get_or_create(customer=customer,complete=False)

#     orderItem,created = OrderItem.objects.get_or_create(order=order,product=product)

#     if action == 'add':
#         orderItem.quantity = (orderItem.quantity + 1)
#     elif action == 'remove':
#         orderItem.quantity = (orderItem.quantity - 1)

#     orderItem.save()

#     if orderItem.quantity <=0:
#         orderItem.delete()

#     return JsonResponse('Item was added',safe=False)