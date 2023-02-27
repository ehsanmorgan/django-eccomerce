from .models import product
from .serialize import productSerialize
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics


@api_view(['GET'])
def peoductList_api(request):
    products=product.objects.all()[:50]
    data=productSerialize(products,many=True,context={'request':request}).data 
    return Response({'data':data})


class productListApi(generics.ListCreateAPIView):
    queryset=product.objects.all() 
    serializer_class=productSerialize 
        
        
        
        
        
class productDetailApi(generics.RetrieveUpdateAPIView):
    queryset=product.objects.all() 
    serializer_class=productSerialize 
    lookup_field='slug'