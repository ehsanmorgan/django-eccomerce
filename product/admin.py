from django.contrib import admin

# Register your models here.
from .models import product,product_image,Brand,reviews



class productImagesAdmin(admin.TabularInline):
    model = product_image


class ReviewsAdmin(admin.ModelAdmin):
    list_display=['user','product','rate','comment','createt_at']
    list_filter=['rate','createt_at']
    search_fields=['user','poriduct','comment']
    


class productAdmin(admin.ModelAdmin):
    list_display=['id','name','brand','price']
    list_filter=['brand','price']
    inlines=[productImagesAdmin]
    list_editable=['name','brand','price']


class brandAdmin(admin.ModelAdmin):
    list_display=['id','name']
    search_fields=['id','name']


admin.site.register(product,productAdmin)
admin.site.register(product_image)
admin.site.register(Brand,brandAdmin)
admin.site.register(reviews,ReviewsAdmin)