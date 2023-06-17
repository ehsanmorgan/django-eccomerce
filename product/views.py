from django.shortcuts import render,redirect
from django.db.models import Count
from django.db.models.aggregates import Sum,Min,Max,Avg
from django.db.models import Value,F,Q,Func,DecimalField,FloatField,ExpressionWrapper
from django.db.models.functions import Concat
from django.views.generic import ListView,DetailView
from .forms import productReviewsForm
from .models import product,reviews
from .models import Brand
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.views.decorators.cache import cache_page
from .fillters import Searchfilter



@cache_page(60*1)
def productlist(request):
    data = product.objects.all()
    return render(request,'product/productlist.html',{'data':data})




class productList(ListView):
    model=product
    paginate_by = 50


class productDetail(DetailView):
    model=product
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["reviews_1"] = reviews.objects.filter(product=self.get_object())
        return context
    

    







def add_review(request,slug):
    product_1=product.objects.get(slug=slug)
    if request.method =='POST':
        form=productReviewsForm(request.POST)
        if form.is_valid():
            myform=form.save(commit=False)
            myform.user=request.user
            myform.product=product_1
            myform.save()

    
            reviews_1=reviews.objects.filter(product=product_1)
            html = render_to_string('include/add_all.html',{'reviews_1':reviews_1 , request:request})
            return JsonResponse({'result':html})


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
    
    





def search_filter(request):
    search_product=product.objects.all()
    myfilter= Searchfilter(request.GET,queryset=search_product)
    context= {'myfilter':myfilter}
    
    return render(request,'search-product.html',context)
    
    

 
def shop_colum4(request):
    shop=product.objects.filter()[:48]
    return render(request,'product/shop-4column.html',{'shop':shop})




 
def shop_colum3(request):
    shop=product.objects.all()[50]
    return render(request,'product/shop-3column.html',{'shop':shop})


def shop_colum2(request):
    shop=product.objects.all()[50]
    return render(request,'product/shop-2column.html',{'shop':shop})


def shop_colum1(request):
    shop=product.objects.all()[50]
    return render(request,'product/shop-1column.html',{'shop':shop})