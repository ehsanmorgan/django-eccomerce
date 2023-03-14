from rest_framework import serializers
from .models import order,order_detail,Cart,cart_detail

class orderserializer(serializers.ModelSerializer):
    class Meta:
        model=order
        fields= ['id','odrder_code','order_status','delivery_date','order_date']
        
        
class orderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model=order_detail
        fields= '__all__'
        
class cartdetailSerializer(serializers.ModelSerializer):
    class Meta:
        model=cart_detail
        fields= ['id','product','price','quantity','total']
        
        
class cartserializer(serializers.ModelSerializer):
    cart_detail=cartdetailSerializer(many=True)
    class Meta:
        model=Cart
        fields='__all__'
        

        
        
