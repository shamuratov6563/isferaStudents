from django.db import models

class ProductImages(models.Model):
    product = models.ForeignKey(' ', on_delete=models.PROTECT)
    color = models.CharField(max_length=100)
    image_1 = models.ImageField(upload_to='ProductImage')
    image_2 = models.ImageField(upload_to='ProductImage')
    image_3 = models.ImageField(upload_to='ProductImage')
    add_price = models.DecimalField(max_digits=10, decimal_places=10)

class ProductMemory(models.Model):
    product = models.ForeignKey('', on_delete=models.PROTECT)
    add_price = models.DecimalField(max_digits=10, decimal_places=10)
    memory  = models.CharField(max_length=100)

class Repair(models.Model):
    title = models.CharField(max_length=100)
    min_price = models.DecimalField(max_digits=10, decimal_places=10)
    repair_time = models.CharField(max_length=100)
    product = models.ForeignKey(' ', on_delete=models.PROTECT)


class RepairAppliction(models.Model):
    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    repair = models.ForeignKey(Repair, on_delete=models.PROTECT)