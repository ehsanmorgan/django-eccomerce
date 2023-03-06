from django_filters import rest_framework as filters

from .models import product,Brand

class productFilter(filters.FilterSet):
    class Meta:
        model=product
        fields={
            'name':['icontains'],
            'price':['lte','gte','range'],
            'brand':['exact'],
            'flag':['exact'],
            'quantity':['range'],
        }
        
        
class brandFilter(filters.FilterSet):
    class Meta:
        model=Brand
        fields={
            'name':['icontains'],
            
        }