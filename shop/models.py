from django.db import models

# Create your models here.

class FAQ(models.Model):

    question = models.CharField(max_length=100)
    answer = models.CharField(max_length=150)

class Email_account(models.Model):

    email = models.EmailField()

    def __str__(self) -> str:
        return self.email


class Category(models.Model):

    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='CategoryImage/')
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self) -> str:
        return self.name

class Product(models.Model):

    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey(Category)
    guarentee = models.CharField(max_length=50)
    support_time = models.CharField(max_length=50)
    pickup = models.CharField(max_length=100)
    available = models.BooleanField()
    delivery_time = models.CharField(max_length=50)
    delivery_cost = models.PositiveIntegerField()
    manufacturer = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self) -> str:
        return self.name

