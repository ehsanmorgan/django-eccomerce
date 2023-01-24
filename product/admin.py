from django.contrib import admin

# Register your models here.
from .models import product,product_image,Brand,reviews

admin.site.register(product)
admin.site.register(product_image)
admin.site.register(Brand)
admin.site.register(reviews)