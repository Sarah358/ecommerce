from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Product)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('title','collection','inventory','price')
    list_editable = ['inventory']
    ordering = ['title','collection']
    search_fields = ['title__istartswith','collection__istartswith']

@admin.register(models.Shippingaddress)
class AddressAdmin(admin.ModelAdmin):
    list_display = [
        'address',
        'street',
        'city',
        'default',
        'country',
    ]


admin.site.register(models.Collection)
admin.site.register(models.Customer)
admin.site.register(models.Order)
admin.site.register(models.OrderItem)
admin.site.register(models.Cart)
admin.site.register(models.CartItem)



