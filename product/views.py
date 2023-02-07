from django.shortcuts import render
from django.db.models import Count

# Create your views here.
from django.views.generic import ListView,DetailView

from .models import product
from .models import Brand


class productList(ListView):
    model=product


class productDetail(DetailView):
    model=product


class brand_list(ListView):
    model=Brand
    queryset=Brand.objects.all().annotate(product_count=Count('product_name'))
   


class brand_detail(DetailView):
    model=Brand