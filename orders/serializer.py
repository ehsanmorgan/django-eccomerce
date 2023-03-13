from rest_framework import serializers
from .models import order,order_detail,Cart,cart_detail

class orderserializer(serializers.ModelSerializer):
    class Meta:
        model=order
        fields='__all__'
        
        
class cartserializer(serializers.ModelSerializer):
    class Meta:
        model=Cart
        fields='__all__'