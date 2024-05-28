from rest_framework import serializers
from .models import Client, ContactApplication, RepairApplication
import django_filters


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

class RepairApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = RepairApplication
        fields = "__all__"