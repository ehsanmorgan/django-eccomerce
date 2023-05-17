from django.shortcuts import render,redirect
from product.models import product as Product
from .models import Cart,cart_detail


# Create your views here.
from django.views.generic import ListView

from .models import order



class order_List(ListView):
    model=order
    
    
    
def add_to_cart(request):
    pass
  





def remover_from_cart(request):
    pass






def chekout(request):
    pass






def invoice(request):
    pass



