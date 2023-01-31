from django.contrib import admin

# Register your models here.
from .models import order,order_detail,Cart, cart_detail


admin.site.register(order)
admin.site.register(order_detail)




admin.site.register(Cart)
admin.site.register(cart_detail)
