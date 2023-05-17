from django.shortcuts import render,redirect
from product.models import product as Product
from .models import Cart,cart_detail


# Create your views here.
from django.views.generic import ListView

from .models import order



class order_List(ListView):
    model=order
    
    
    
def add_to_cart(request):
    quantity=request.POST['quantity']
    product=Product.objects.get(id=request.POST['product_id'])
    cart=Cart.objects.get(user=request.user , cart_status='Inprogress')
    cart_details,created=cart_detail.objects.get_or_create(cart=cart , product=product)
    cart_details.quantity=quantity
    cart_details.price=product.price
    cart_details.total = int(quantity) * product.price
    cart_details.save()
    return redirect(f'/products/{product.slug}')





def remover_from_cart(request,id):
    cart_details=cart_detail.objects.get(id=id)
    cart_details.delete()
    return redirect('/products')






def chekout(request):
    cart=Cart.objects.get(user=request.user , cart_status='Inprogress')
    cart_details=cart_detail.objects.filter(cart=cart)
    
    
    delivery_fee = 5
    total =  delivery_fee + cart.total_cart()
    sub_total= cart.total_cart()

    
    
    return render(request,'orders/checkout.html',{'cart':cart, 'cart_details':cart_details , 'delivery_fee':delivery_fee ,'total':total })






def invoice(request):
    pass



