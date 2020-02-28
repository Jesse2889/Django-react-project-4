from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Product, Like, Basket
User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'

class LikeSerializer(serializers.ModelSerializer):
    owner = UserSerializer()
    class Meta:
        model = Like
        fields = '__all__'       

class BasketSerializer(serializers.ModelSerializer):

    class Meta:
        model = Basket
        fields = '__all__'  

class PopulatedLikeSerializer(LikeSerializer):
    owner = UserSerializer()

class PopulatedBasketSerializer(BasketSerializer):
    products = ProductSerializer(many=True)
    likes = PopulatedLikeSerializer(many=True)
