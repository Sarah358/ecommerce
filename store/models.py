
from ast import Or
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.forms import ModelForm
from django.shortcuts import reverse


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
    slug = models.SlugField()


    # exception handling for image url
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        
        return url

    # changing str rep
    def __str__(self) -> str:
        return self.title
       
    def get_absolute_url(self):
        return reverse("product_details", kwargs={"slug": self.slug})
    
    def get_add_to_cart_url(self):
        return reverse("add-to-cart", kwargs={"slug": self.slug})
    def get_remove_from_cart_url(self):
        return reverse("remove-from-cart", kwargs={"slug": self.slug})
    
    
    
    
    # sort collection
    class Meta:
        ordering = ['id']


# update inventory model form 
class Updateinventory(ModelForm):
    class Meta:
        model = Product
        fields = ['inventory']


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




# orderitem
class OrderItem(models.Model):
    # order = models.ForeignKey(Order,on_delete=models.PROTECT)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE,null=True,blank=True)
    product = models.ForeignKey(Product,on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField(default=1)
    complete = models.BooleanField(max_length=1,default=False,null=True)


         # changing str rep
    def __str__(self) -> str:
        return f"{self.quantity} of {self.product.title}"
    
    # get total
    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total
    @property
    def get_total_orderitems(self):
        orderitems = self.order

# order
class Order(models.Model):
    placed_at = models.DateField(auto_now_add=True,null=True)
    complete = models.BooleanField(max_length=1,default=False,null=True)
    customer = models.ForeignKey(Customer,on_delete=models.PROTECT,null=True,default='sarah')
    products = models.ManyToManyField(OrderItem)


        # changing str rep
    def __str__(self) -> str:
        return str(self.id)
    # get cart total
    @property
    def get_cart_total(self):
        orderitems = self.products.all()
        total = sum([item.get_total for item in orderitems])
        return total
    
    # get cart items
    @property
    def get_cart_items(self):
        orderitems = self.products.all()
        total = sum([item.quantity for item in orderitems])
        return total






class Shippingaddress(models.Model):
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