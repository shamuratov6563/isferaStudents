from django.shortcuts import render
from . import serializer
from rest_framework.generics import ListAPIView
from . import models
from rest_framework import generics
from .models import Client, ContactApplication
from .serializers import ClientSerializer, ClientFilter, AplicationSerializer, RepairApplicationSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView,CreateAPIView
from .models import Discount,Faq
from .serializers import DiscountSerializer,FrequentlyAskedQuestionsSerializer


class FAQListAPIView(ListAPIView):
    serializer_class = serializer.FAQSerializer
    queryset = models.Faq.objects.all()


class RepairListAPIView(ListAPIView):
    serializer_class = serializer.RepairSerializer
    queryset = models.Repair.objects.all()


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


class RepairAppCreateAPIView(generics.CreateAPIView):
    serializer_class = RepairApplicationSerializer
    queryset = models.RepairApplication.objects.all()

    
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
