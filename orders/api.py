from rest_framework import generics
from .models import order,order_detail,cart_detail,Cart
from .serializer import orderserializer,cartserializer
from django.contrib.auth.models import User
from rest_framework.response import Response


class orderListAPI(generics.ListAPIView):
    queryset=order.objects.all()
    serializer_class=orderserializer
    
    
    
    
    
    
class cartdetailAPI(generics.RetrieveDestroyAPIView):
    def get(self,request,*args,**kwargs):
        user_name=self.kwargs['username']
        user=User.objects.get(username=user_name)
        cart=Cart.objects.get(user=user,cart_status='Inprogress')
        data=cartserializer(cart).data
        return Response({'cart':data})