from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Product)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('title','collection','inventory','price')
    list_editable = ['price']
    ordering = ['title','collection']
    search_fields = ['title__istartswith','collection__istartswith']


admin.site.register(models.Collection)

