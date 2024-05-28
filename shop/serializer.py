from . import models
from rest_framework import serializers

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Category
        fields = (
            'id',
            'name',
        )

class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = (    
            'name',
        )

class RepairSerializer(serializers.ModelSerializer):
    product = ProductListSerializer()
    class Meta:
        model = models.Repair
        fields = (
            'id',
            'title',
            'min_price',
            'repair_time',
            'product',
        )




class FAQSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.FAQ
        fields = '__all__'







