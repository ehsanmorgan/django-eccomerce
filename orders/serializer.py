from rest_framework import serializers
from .models import order,order_detail,Cart,cart_detail


class orderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model=order_detail
        fields= '__all__'

class orderserializer(serializers.ModelSerializer):
    order_detail=orderDetailSerializer(source='odere_detail',many=True)
    class Meta:
        model=order
        fields= ['id','odrder_code','order_status','delivery_date','order_date','order_detail']
        
        

        
class cartdetailSerializer(serializers.ModelSerializer):
    class Meta:
        model=cart_detail
        fields= ['id','product','price','quantity','total']
        
        
class cartserializer(serializers.ModelSerializer):
    cart_detail=cartdetailSerializer(many=True)
    class Meta:
        model=Cart
        fields='__all__'
        

        
        
