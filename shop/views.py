from django.shortcuts import render
from . import serializer
from rest_framework.generics import ListAPIView
from . import models
from rest_framework import generics
from .models import Client, ContactApplication
from .serializers import ClientSerializer, ClientFilter, AplicationSerializer
from django_filters.rest_framework import DjangoFilterBackend


class FAQListAPIView(ListAPIView):
    serializer_class = serializer.FAQSerializer
    queryset = models.FAQ.objects.all()


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
