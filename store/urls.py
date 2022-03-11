from django.urls import path
from . import views
from .views import Homeview,ProductDetailView,CheckoutView,PaymentView

urlpatterns = [
    # path('products',views.index, name='home'),
    path('',Homeview.as_view(), name='template'),
    path('cart/',views.cart, name='cart'),
    path('add-to-cart/<slug>/',views.add_to_cart, name='add-to-cart'),
    path('remove-from-cart/<slug>/',views.remove_from_cart, name='remove-from-cart'),
    path('reduce-cart-quantity/<slug>/',views.reduce_cart_quantity, name='reduce-cart-quantity'),
    path('checkout/',CheckoutView.as_view(), name='checkout'),
    path('payment/<payment_option>',PaymentView.as_view(), name='payment'),
    path('product/<slug>/',ProductDetailView.as_view(),name='product_details'),
    path('reduce_inventory/<str:pk>/',views.reduce_inventory,name='reduce_inventory'),
    path('login/',views.login, name='login'),
    path('register/',views.register, name='register'),
    


]
