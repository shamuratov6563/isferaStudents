from django.contrib import admin

from . import models
from .models import Client, ContactApplication, Discount,Faq

admin.site.register(models.Faq)
admin.site.register(models.Repair)
admin.site.register(models.Product)
admin.site.register(models.Category)
admin.site.register(Client)
admin.site.register(ContactApplication)
admin.site.register(Discount)