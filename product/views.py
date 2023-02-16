from django.shortcuts import render,redirect
from django.db.models import Count
from django.db.models.aggregates import Sum,Min,Max,Avg
from django.db.models import Value,F,Q,Func,DecimalField,FloatField,ExpressionWrapper
from django.db.models.functions import Concat
from django.views.generic import ListView,DetailView
from .forms import productReviewsForm
from .models import product
from .models import Brand







class productList(ListView):
    model=product
    paginate_by = 50


class productDetail(DetailView):
    model=product




def add_review(request,slug):
    product_1=product.objects.get(slug=slug)
    if request.method =='POST':
        form=productReviewsForm(request.POST)
        if form.is_valid():
            myform=form.save(commit=False)
            myform.user=request.user
            myform.product=product_1
            myform.save()

    return redirect (f'/products/{product_1.slug}')


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