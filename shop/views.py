from django.shortcuts import render
from . import serializer
from rest_framework.generics import ListAPIView
from . import models


class FAQListAPIView(ListAPIView):

    serializer_class = serializer.FAQSerializer
    queryset = models.FAQ.objects.all()


class ProductListAPIView(ListAPIView):
    
    serializer_class = serializer.RepairSerializer
    queryset = models.Product.objects.all()


class CategoryListAPIView(ListAPIView):
    
    serializer_class = serializer.CategorySerializer
    queryset = models.Category.objects.all()
