from django.db import models
from django.contrib import admin
from django.contrib.auth import get_user_model
User = get_user_model()

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.CharField(max_length=5)
    image = models.CharField(max_length=300)
    description = models.CharField(max_length=300)
    

    def __str__(self):
        return f'{self.name}'

class Like(models.Model):
    like = models.IntegerField(default=0)
    owner = models.ForeignKey(User, related_name='likes', null=True, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name="likes", null=True, on_delete=models.CASCADE)   

    def __str__(self):
      return f'Like by {self.owner} on {self.product}'     

class Basket(models.Model):
    products = models.ForeignKey(Product, related_name='basket', blank=True, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, related_name='basket', blank=True, on_delete=models.CASCADE)