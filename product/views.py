from django.shortcuts import render
from django.db.models import Count

# Create your views here.
from django.views.generic import ListView,DetailView

from .models import product
from .models import Brand


class productList(ListView):
    model=product
    paginate_by = 1


class productDetail(DetailView):
    model=product


class brand_list(ListView):
    model=Brand
    paginate_by = 1
    queryset=Brand.objects.all().annotate(product_count=Count('product_name'))
   


class brand_detail(DetailView):
    model=Brand
    

    def get_queryset(self):
        queryset=Brand.objects.filter(slug=self.kwargs['slug']).annotate(product_count=Count('product_name'))

        return queryset