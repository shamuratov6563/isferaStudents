from django.shortcuts import render
from rest_framework import generics
from .models import Client, ContactApplication
from .serializers import ClientSerializer, ClientFilter, AplicationSerializer
from django_filters.rest_framework import DjangoFilterBackend


class ContactApplicationCreateView(generics.CreateAPIView):
    queryset = ContactApplication.objects.all()
    serializer_class = AplicationSerializer



class ClientListAPIView(generics.ListAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ClientFilter


