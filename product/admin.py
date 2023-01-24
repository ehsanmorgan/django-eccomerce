from django.contrib import admin

# Register your models here.
from .models import product,product_image,Brand,reviews



class productImagesAdmin(admin.TabularInline):
    model = product_image


class productAdmin(admin.ModelAdmin):
    list_display=['name','brand','price']
    list_filter=['brand','price']
    inlines=[productImagesAdmin]

admin.site.register(product,productAdmin)
admin.site.register(product_image)
admin.site.register(Brand)
admin.site.register(reviews)