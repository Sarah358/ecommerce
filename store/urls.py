from django.urls import path
from . import views
from .views import Homeview

urlpatterns = [
    # path('products',views.index, name='home'),
    path('',Homeview.as_view(), name='template'),
    path('cart',views.cart, name='cart'),
    path('checkout',views.checkout, name='checkout'),
    path('update_item/',views.updateItem, name='update_item'),
    path('<int:product_id>',views.product_details,name='product_details'),
    path('reduce_inventory/<str:pk>/',views.reduce_inventory,name='reduce_inventory')
]
