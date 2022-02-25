
from ast import Or
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator


# Create your models here.
class Collection(models.Model):
    title = models.CharField(max_length=255)
    featured_product = models.ForeignKey('Product',on_delete=models.SET_NULL,null=True,related_name='+',blank=True)
    
    # changing str rep
    def __str__(self) -> str:
        return self.title
    
    # sort collection
    class Meta:
        ordering = ['title']

class Product(models.Model):
    title = models.CharField(max_length=255)
    description= models.TextField(null=True,blank=True )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=3,
        validators= [MinValueValidator(1)]
        )
    inventory= models.IntegerField(null=True)
    last_update = models.DateTimeField(auto_now=True)
    collection = models.ForeignKey(Collection,on_delete=models.PROTECT)
    image = models.ImageField(null=True,blank = True)
    

    # changing str rep
    def __str__(self) -> str:
        return self.title
    
    # sort collection
    class Meta:
        ordering = ['id']


# customers model
class Customer(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email=models.EmailField(unique=True)
    phone = models.CharField(max_length=255)
    birth_date = models.DateField(null=True)
   

     # changing str rep
    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
    
    # sort collection
    class Meta:
        ordering = ['first_name','last_name']

# order
class Order(models.Model):
    PAYMENT_STATUS_PENDING = 'P'
    PAYMENT_STATUS_COMPLETE = 'C'
    PAYMENT_STATUS_FAILED = 'F'

    PAYMENT_STATUS_CHOICES =[
        (PAYMENT_STATUS_PENDING,'Pending'),
        (PAYMENT_STATUS_COMPLETE,'Complete'),
        (PAYMENT_STATUS_FAILED,'Failed'),

    ]
    placed_at = models.DateField(auto_now_add=True)
    payment_status = models.CharField(
        max_length=1,choices=PAYMENT_STATUS_CHOICES,default=PAYMENT_STATUS_PENDING
    )
    customer = models.ForeignKey(Customer,on_delete=models.PROTECT)

        # changing str rep
    def __str__(self) -> str:
        return self.id

# orderitem
class OrderItem(models.Model):
    order = models.ForeignKey(Order,on_delete=models.PROTECT)
    product = models.ForeignKey(Product,on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=6,decimal_places=2)

         # changing str rep
    def __str__(self) -> str:
        return self.id

class Shippingddress(models.Model):
    address = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    order = models.ForeignKey(Order,on_delete=models.SET_NULL,blank=True,null=True)
    date_added = models.DateTimeField(auto_now_add=True)

         # changing str rep
    def __str__(self) -> str:
        return self.address

class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

          # changing str rep
    def __str__(self) -> str:
        return self.id

class CartItem(models.Model):
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()

          # changing str rep
    def __str__(self) -> str:
        return self.id