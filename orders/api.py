from rest_framework import generics
from .models import order,order_detail,cart_detail,Cart
from .serializer import orderserializer,cartserializer
from django.contrib.auth.models import User
from rest_framework.response import Response
from product.models import product as Product


class orderListAPI(generics.ListAPIView):
    queryset=order.objects.all()
    serializer_class=orderserializer
    
    
    
    
    
    
    
    
class cartdetailAPI(generics.RetrieveDestroyAPIView):
    def get(self,request,*args,**kwargs):
        user_name=self.kwargs['username']
        user=User.objects.get(username=user_name)
        cart,created=Cart.objects.get_or_create(user=user,cart_status='Inprogress')
        data=cartserializer(cart).data
        return Response({'cart':data})
    
    
    def post(self,request,*args,**kwargs):
        user_name=self.kwargs['username']
        user=User.objects.get(username=user_name)
        product_11=Product.objects.get(id=request.data['product_id'])
        quantity=int(request.data['quantity'])
        cart1=Cart.objects.get(user=user,cart_status='Inprogress')
        cart_data,created=cart_detail.objects.get_or_create(cart=cart1 ,product=product_11 )
        cart_data.price=product.price
        cart_data.quantity=quantity
        cart_data.total=quantity*price
        