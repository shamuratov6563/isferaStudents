from rest_framework import serializers
from .models import Discount,Faq
from rest_framework import serializers
from .models import Client, ContactApplication,Product
import django_filters

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

class ProductFilterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['category', 'name']

class ProductFilter(django_filters.FilterSet):
    class Meta:
        model = Product
        fields = ['name']