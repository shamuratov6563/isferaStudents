from django.shortcuts import render
from . import serializers
from rest_framework.generics import ListAPIView
from . import models
from rest_framework import generics
from .models import Client, ContactApplication, Email_account
from .serializers import ClientSerializer, ClientFilter, AplicationSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView,CreateAPIView
from .models import Discount,Faq
from .serializers import DiscountSerializer,FrequentlyAskedQuestionsSerializer, EmailSerializer


class FAQListAPIView(ListAPIView):
    serializer_class = serializers.FAQSerializer
    queryset = models.Faq.objects.all()


class ProductListAPIView(ListAPIView):
    serializer_class = serializers.ProductListSerializer
    queryset = models.Product.objects.all()


class ContactApplicationCreateView(generics.CreateAPIView):
    queryset = ContactApplication.objects.all()
    serializer_class = AplicationSerializer

class EmailCreateView(generics.CreateAPIView):
    queryset = Email_account.objects.all()
    serializer_class = EmailSerializer


class CategoryListAPIView(ListAPIView):
    serializer_class = serializers.CategorySerializer
    queryset = models.Category.objects.all()

class CategoryListWithImage(ListAPIView):
    serializer_class = serializers.CategorySerializer
    queryset = models.Category.objects.all()

class ClientListAPIView(generics.ListAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ClientFilter

class DiscountListView(ListAPIView):
    queryset = Discount.objects.all()
    serializer_class = DiscountSerializer

class DiscountCreateAPIView(CreateAPIView):
    queryset = Discount.objects.all()
    serializer_class = DiscountSerializer


class FaqListView(ListAPIView):
    queryset = Faq.objects.all()
    serializer_class = FrequentlyAskedQuestionsSerializer

class FaqCreateAPIView(CreateAPIView):
    queryset = Faq.objects.all()
    serializer_class = FrequentlyAskedQuestionsSerializer
