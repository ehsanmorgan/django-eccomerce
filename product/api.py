from .models import product,Brand
from .serialize import productListSerialize,productDetailSerialize,brandListSerializer,brandDetailSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from .pagenation import mypage
import django_filters.rest_framework
from .myfillters import productFilter,brandFilter



@api_view(['GET'])
def peoductList_api(request):
    products=product.objects.all()[:50]
    data=productListSerialize(products,many=True,context={'request':request}).data 
    return Response({'data':data})


class productListApi(generics.ListCreateAPIView):
    queryset=product.objects.all() 
    serializer_class=productListSerialize 
    pagination_class=mypage
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields=['name','brand','flag','price']
    filterset_class=productFilter
    
    
    


        
        
        
        
        
class productDetailApi(generics.RetrieveUpdateDestroyAPIView):
    queryset=product.objects.all() 
    serializer_class=productDetailSerialize 
    lookup_field='slug'
    
    
    
class BrandListApi(generics.ListAPIView):
    queryset=Brand.objects.all()
    serializer_class=brandListSerializer 
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_class=brandFilter
    
    
class BrandDetailView(generics.RetrieveAPIView):
    queryset=Brand.objects.all()
    serializer_class=brandDetailSerializer 
    lookup_field='slug'
        