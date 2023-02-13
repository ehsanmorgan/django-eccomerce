from django.shortcuts import render
from django.db.models import Count

# Create your views here.
from django.views.generic import ListView,DetailView

from .models import product
from .models import Brand






def query_debug(request):
    data=product.objects.filter().order_by ('-name')
    return render(request,'product/productlist.html',{'data':data})


class productList(ListView):
    model=product
    paginate_by = 50


class productDetail(DetailView):
    model=product


class brand_list(ListView):
    model=Brand
    paginate_by = 20
    queryset=Brand.objects.all().annotate(product_count=Count('product_name'))
   


class brand_detail(ListView):
    model=product
    paginate_by = 50
    template_name='product/brand_detail.html'


    def get_queryset(self):
        brand=Brand.objects.get(slug=self.kwargs['slug'])
        queryset=product.objects.filter(brand=brand)
        return queryset


    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        data=Brand.objects.filter(slug=self.kwargs['slug']).annotate(product_count=Count('product_name'))[0]
        print(f'Brand:{data.name}')
        print(f'Brand:{data.image}')
        context['brand']=data
        return context