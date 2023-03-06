from rest_framework import serializers
from .models import product,Brand


class brandSerializer(serializers.ModelSerializer):
    class Meta:
        model=Brand
        fields='__all__'

class productSerialize(serializers.ModelSerializer):
    brand=brandSerializer()

    class Meta:
        model = product
        fields= '__all__'
        
        
