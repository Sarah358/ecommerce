from django.urls import path
from . import views
from .views import Homeview,ProductDetailView,CheckoutView

urlpatterns = [
    # path('products',views.index, name='home'),
    path('',views.index, name='template'),
    path('cart/',views.cart, name='cart'),
    path('shop/',views.shop, name='shop'),
    path('contact/',views.contact, name='contact'),
    path('about/',views.about, name='about'),
    path('faq/',views.faq, name='faq'),
    path('add-to-cart/<slug>/',views.add_to_cart, name='add-to-cart'),
    path('remove-from-cart/<slug>/',views.remove_from_cart, name='remove-from-cart'),
    path('reduce-cart-quantity/<slug>/',views.reduce_cart_quantity, name='reduce-cart-quantity'),
    path('checkout/',CheckoutView.as_view(), name='checkout'),
    path('product/<slug>/',ProductDetailView.as_view(),name='product_details'),
      path('collection-product-list/<int:col_id>',views.collection_product_list,name='collection-product-list'),
    path('reduce_inventory/<str:pk>/',views.reduce_inventory,name='reduce_inventory'),
    path('my-dashboard',views.my_dashboard, name='my_dashboard'),
    path('my-orders',views.my_orders, name='my_orders'),
    path('my-orders-items/<int:id>',views.my_order_items, name='my_order_items'),
    
    


]
