from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class customUser(AbstractUser):
    email = models.EmailField()
    phone = models.CharField(max_length=10)