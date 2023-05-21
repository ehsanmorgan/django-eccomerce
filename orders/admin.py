from django.contrib import admin

# Register your models here.
from .models import order,order_detail,Cart, cart_detail,Coupon


class orderAdmin(admin.ModelAdmin):
    list_display=['odrder_code','delivery_date']
    list_filter=['order_status','order_date']

class order_detailAdmin(admin.ModelAdmin):
    list_display=['order','product','price','quantity','total']
    list_filter=['price','quantity']
 
admin.site.register(order,orderAdmin)
admin.site.register(order_detail,order_detailAdmin)






admin.site.register(Cart)
admin.site.register(Coupon)

admin.site.register(cart_detail)
