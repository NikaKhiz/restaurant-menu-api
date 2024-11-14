from rest_framework import serializers
from .models import Restaurant, Menu

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ('id', 'name', 'address', 'phone_number', 'image')
        extra_kwargs = {'address': {'write_only': True}, 'phone_number': {'write_only': True}, 'image': {'write_only': True}}

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['id', 'name', 'image', 'parent', 'restaurant']
        extra_kwargs = {'image': {'write_only': True}, 'parent': {'write_only': True}, 'restaurant': {'write_only': True}}

class SubMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['name', 'image', 'parent', 'restaurant']
        extra_kwargs = {'id': {'write_only': True}, 'parent': {'write_only': True}, 'restaurant': {'write_only': True}}
        