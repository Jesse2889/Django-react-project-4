from django.db import models
from django.contrib import admin

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.CharField(max_length=5)
    image = models.CharField(max_length=300)
    description = models.CharField(max_length=300)

    def __str__(self):
        return f'{self.name}'