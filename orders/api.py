from rest_framework import generics
from .models import order,order_detail,cart_detail,Cart
from .serializer import orderserializer,cartserializer,cartdetailSerializer
from product.models import product as Product
from django.contrib.auth.models import User
from rest_framework.response import Response



class orderListAPI(generics.ListAPIView):
    queryset=order.objects.all()
    serializer_class=orderserializer
    
    
    
    
    
    
    
    
class cartdetailAPI(generics.RetrieveDestroyAPIView):
    serializer_class=cartdetailSerializer
    def get(self,request,*args,**kwargs):
        user_name=self.kwargs['username']
        user=User.objects.get(username=user_name)
        cart,created=Cart.objects.get_or_create(user=user,cart_status='Inprogress')
        data=cartserializer(cart).data
        return Response({'cart':data})
    
    
    def post(self,request,*args,**kwargs):
        user_name=self.kwargs['username']
        user=User.objects.get(username=user_name)
        product_id=Product.objects.get(id=request.data['product_id'])
        quantity=int(request.data['quantity'])
        cart1=Cart.objects.get(user=user,cart_status='Inprogress')
        cart_data,created=cart_detail.objects.get_or_create(cart=cart1 , product=product_id )
        cart_data.price=product_id.price
        cart_data.quantity=quantity
        cart_data.total=round(quantity*product_id.price,2)
        cart_data.save()
        return Response({'status':200})
    
    
    def delete(self,request,*args,**kwargs):
        user=User.objects.get(username=self.kwargs['username'])
        product_id=Product.objects.get(id=request.data['product_id'])
        cart1=Cart.objects.get(user=user,cart_status='Inprogress')
        cart_data=cart_detail.objects.get(cart=cart1 , product=product_id )
        cart_data.delete()
        return Response({'status':200,'massage':'deleted successfully '})

        
        