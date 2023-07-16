from django.contrib import admin
from tof.admin import TofAdmin, TranslationTabularInline
from tof.decorators import tof_prefetch
from .models import product,product_image,Brand,reviews,WishProduct






class productImagesAdmin(admin.TabularInline):
    model = product_image


class productadmin1(admin.ModelAdmin):
    list_display=['id','name','flag']
    list_filter=['name','flag']
    search_fields=['name','flag']








class ReviewsAdmin(admin.ModelAdmin):
    list_display=['user','product','rate','comment','createt_at']
    list_filter=['rate','createt_at']
    search_fields=['product__name','comment']
    
    




class brandAdmin(admin.ModelAdmin):
    list_display=['id','name']
    search_fields=['id','name']
    
admin.site.register(product,productadmin1)
admin.site.register(product_image)
admin.site.register(Brand,brandAdmin)
admin.site.register(reviews,ReviewsAdmin)
admin.site.register(WishProduct)
