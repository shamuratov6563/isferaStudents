from django.db import models

class ContactApplication(models.Model):
  full_name = models.CharField(max_length=100)
  phone_number = models.CharField(max_length=20)
  
  def __str__(self):
        return f"{self.id}-{self.full_name}"
  

class Discount(models.Model):
  title= models.CharField(max_length=100)
  percentage = models.PositiveIntegerField()
  image = models.ImageField(upload_to='discount')
  link = models.URLField()

  def __str__(self):
        return f"{self.id}-{self.title}"

class Client(models.Model):
  class ClientChoices(models.Choices):
      STARS = 'stars', 'Stars'
      COMPANY = 'company',"Company"
  name= models.CharField(max_length=100)
  position = models.CharField(max_length=50)
  image = models.ImageField(upload_to='discount')
  type = models.CharField(max_length=50, choices=ClientChoices.choices, default=ClientChoices.STARS)

  def __str__(self):
        return f"{self.id}-{self.name}"


