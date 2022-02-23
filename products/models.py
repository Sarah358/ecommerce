from django.db import models
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
    

    # changing str rep
    def __str__(self) -> str:
        return self.title
    
    # sort collection
    class Meta:
        ordering = ['title']
