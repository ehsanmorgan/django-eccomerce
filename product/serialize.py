from rest_framework import serializers
from .models import product,Brand





class productSerialize(serializers.ModelSerializer):
    #brand=brandSerializer()
    brand=serializers.StringRelatedField()
    pirce_tex=serializers.SerializerMethodField('myprice')

    class Meta:
        model = product
        fields= '__all__'
        
        
    def myprice(self,product):
        return product.price * 1.1


class brandListSerializer(serializers.ModelSerializer):
    class Meta:
        model=Brand
        fields='__all__'
        

class brandDetailSerializer(serializers.ModelSerializer):
    products = productSerialize (source = 'product_name',many=True)
    class Meta:
        model=Brand
        fields='__all__'


        
        
