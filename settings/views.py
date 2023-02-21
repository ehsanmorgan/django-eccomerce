from django.shortcuts import render
from product.models import Brand,product,reviews
from django.db.models import Count

# Create your views here.


def home(request):
    item_sale=product.objects.filter(flag='Sale')[:10]
    item_feature=product.objects.filter(flag='Feature')[:6]
    item_new=product.objects.filter(flag='New')[:12]
    reviews_2_=reviews.objects.all()
    brands=Brand.objects.all().annotate(product_count=Count('product_name'))
    return render(request,'settings/home.html',{
        'brands':brands,
        'item_sale':item_sale,
        'item_feature':item_feature,
        'item_new':item_new,
        'reviews_2_':reviews_2_
        })