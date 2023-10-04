from django.db import models

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=25)
    picture = models.ImageField()
    author = models.CharField(max_length=30, default='Anonymous')
    email = models.EmailField(blank=True)
    describe = models.TextField(default='Data flair tutorial')


class user(models.Model):
    username = models.CharField(max_length=25)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=255)