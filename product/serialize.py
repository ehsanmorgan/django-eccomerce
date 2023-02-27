from rest_framework import serializers
from .models import product


class productSerialize(serializers.ModelSerializer):

    class Meta:
        model = product
        fields= '__all__'
        