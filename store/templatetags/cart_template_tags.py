from django import template
from store.models import Order

# register template tags
register = template.Library()

@register.filter
def cart_items_count(user):
    if user.is_authenticated:
        customer = request.user.customer
        qs = Order.objects.filter(user=user,complete=False)
        if qs.exists():
            return qs[0].products.count()
    return 0
            
