from rest_framework import serializers
from .models import product,Brand,product_image,reviews



class imagesSerializer(serializers.ModelSerializer):
    class Meta:
        model=product_image
        fields=['image']



class productListSerialize(serializers.ModelSerializer):
    #brand=brandSerializer()
    brand=serializers.StringRelatedField()
    pirce_tex=serializers.SerializerMethodField('myprice')
    
    review_count=serializers.SerializerMethodField()

    class Meta:
        model = product
        fields= '__all__'
        
    def get_review_count(self,product):
        review=product.product_review.all().count()
        return review
        
        
    def myprice(self,product):
        return product.price * 1.1

class ReviewSerializer(serializers.ModelSerializer):
    user=serializers.StringRelatedField()
    class Meta:
        model=reviews
        fields= ['comment','rate','createt_at','user']


class productDetailSerialize(serializers.ModelSerializer):
    brand=serializers.StringRelatedField()
    image=imagesSerializer(source='product_image',many=True)
    review_count=serializers.SerializerMethodField()
    review=ReviewSerializer(source='product_review',many=True)
    

    class Meta:
        model = product
        fields= '__all__'
        
        
    def get_review_count(self,product):
        review=product.product_review.all().count()
        return review
  
    

    
    
    
    
    
    
    
    

class brandListSerializer(serializers.ModelSerializer):
    class Meta:
        model=Brand
        fields='__all__'
        

class brandDetailSerializer(serializers.ModelSerializer):
    products = productListSerialize (source = 'product_name',many=True)
    class Meta:
        model=Brand
        fields='__all__'


        
        
