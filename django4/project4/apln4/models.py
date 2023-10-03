from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustUser(AbstractUser):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.EmailField()
    phone = models.CharField(max_length=10)