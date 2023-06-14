import django_filters
from .models import product as Product

class Searchfilter(django_filters.FilterSet):
    class Meta:
        model=Product
        fields= ['name','price','brand']