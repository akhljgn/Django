from django.db import models

# Create your models here.
class user(models.Model):
    username = models.CharField(max_length=25)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=255)