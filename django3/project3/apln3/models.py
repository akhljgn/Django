from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=25)
    age = models.IntegerField()
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=10)