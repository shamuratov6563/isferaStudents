from django.shortcuts import render
from . import serializer
from rest_framework.generics import ListAPIView
from . import models
from rest_framework import generics
from .models import Client, ContactApplication
from .serializers import ClientSerializer, ClientFilter, AplicationSerializer,ProductFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView,CreateAPIView
from .models import Discount,Faq,Product
from .serializers import DiscountSerializer,FrequentlyAskedQuestionsSerializer,ProductFilterSerializer


class FAQListAPIView(ListAPIView):
    serializer_class = serializer.FAQSerializer
    queryset = models.Faq.objects.all()


class ProductListAPIView(ListAPIView):
    serializer_class = serializer.RepairSerializer
    queryset = models.Product.objects.all()


class ContactApplicationCreateView(generics.CreateAPIView):
    queryset = ContactApplication.objects.all()
    serializer_class = AplicationSerializer


class CategoryListAPIView(ListAPIView):
    serializer_class = serializer.CategorySerializer
    queryset = models.Category.objects.all()


class ClientListAPIView(generics.ListAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ClientFilter

class DiscountListView(ListAPIView):
    queryset = Discount.objects.all()
    serializer_class = DiscountSerializer


class FaqListView(ListAPIView):
    queryset = Faq.objects.all()
    serializer_class = FrequentlyAskedQuestionsSerializer

class ProductfilterListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductFilterSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductFilter


