from django.contrib import admin

from . import models

admin.site.register(models.FAQ)
admin.site.register(models.Repair)
admin.site.register(models.Product)
admin.site.register(models.Category)
