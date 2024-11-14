from rest_framework import serializers
from .models import Restaurant

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ('id', 'name', 'address', 'phone_number', 'image')
        extra_kwargs = {'address': {'write_only': True}, 'phone_number': {'write_only': True}, 'image': {'write_only': True}}

