from rest_framework import serializers
from .models import Discount,Faq
from .models import Client, ContactApplication, Email_account, Statiy
from rest_framework import serializers
from .models import Client, ContactApplication, RepairApplication
from .models import Client, ContactApplication,Product
import django_filters
from . import models



class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Category
        fields = (
            'id',
            'name',
            'image',
        )
class RepairSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Repair
        fields = (
            'id',
            'title',
            'min_price',
            'repair_time',
        )

class ProductListSerializer(serializers.ModelSerializer):
    repair = RepairSerializer()
    class Meta:
        model = models.Product
        fields = (
            'name',
            'repair',
        )


class RepairSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Repair
        fields = (
            'id',
            'title',
            'min_price',
            'repair_time',
        )


class FAQSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Faq
        fields = '__all__'


class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = ['id', 'title', 'percentage', 'image', 'link']

class FrequentlyAskedQuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faq
        fields = ['id', 'question', 'answer']

class ClientFilter(django_filters.FilterSet):
    class Meta:
        model = Client
        fields = ['type']


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'name', 'position', 'image', 'type']

class AplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactApplication
        fields = "__all__"
        
        
class StatiySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Statiy
        fields = "__all__"

class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Email_account
        fields = ['email',]

class RepairApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = RepairApplication
        fields = "__all__"


class ProductMemorySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.ProductMemory
        fields = ('id', 'memory', 'add_price')


class ProductColorSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.ProductColor
        exclude = ('product',)


class ProductListSerializer(serializers.ModelSerializer):
    poster = serializers.SerializerMethodField()
    product_memories = ProductMemorySerializer(many=True)
    product_colors = ProductColorSerializer(many=True)

    def get_poster(self, obj):
        if obj.product_images.first():
            return obj.product_images.first().image_1.url
        return None

    class Meta:
        model = models.Product
        fields = ('id', 'name', 'description', 'price', 'poster', 'product_memories', 'product_colors')

class ProductFilterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['category', 'name']

class ProductFilter(django_filters.FilterSet):
    class Meta:
        model = Product
        fields = ['name']