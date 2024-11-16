from rest_framework import serializers
from .models import Restaurant, Menu, Dish, Ingredient
from django.db import transaction

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ('id', 'name', 'address', 'phone_number', 'image')
        extra_kwargs = {'address': {'write_only': True}, 'phone_number': {'write_only': True}, 'image': {'write_only': True}}

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['id', 'name']

class DishSerializer(serializers.ModelSerializer):
    ingredients = IngredientSerializer(many=True)

    class Meta:
        model = Dish
        fields = ['id', 'name', 'price', 'image', 'menu', 'ingredients']
    
    def create(self, validated_data):
        ingredients_data = validated_data.pop('ingredients', [])
        with transaction.atomic():
            dish = Dish.objects.create(**validated_data)
            for ingredient_data in ingredients_data:
                ingredient, created = Ingredient.objects.get_or_create(name=ingredient_data['name'])
                dish.ingredients.add(ingredient)
        return dish

    def update(self, instance, validated_data):
        ingredients_data = validated_data.pop('ingredients', [])
        with transaction.atomic():
            # update the fields of the dish
            for attr, value in validated_data.items():
                setattr(instance, attr, value)
            instance.save()

            existing_ingredients = set(instance.ingredients.all())
            new_ingredients = set()
            for ingredient_data in ingredients_data:
                ingredient, created = Ingredient.objects.get_or_create(name=ingredient_data['name'])
                new_ingredients.add(ingredient)

            # remove ingredients that are no longer presented
            ingredients_to_remove = existing_ingredients - new_ingredients
            for ingredient in ingredients_to_remove:
                ingredient_instance = Ingredient.objects.get(name=ingredient)
                instance.ingredients.remove(ingredient)
                # remove ingrediensdt from the db if ingredient is not associated with another dish
                if not ingredient_instance.dish.exists():
                    ingredient_instance.delete()

            # add new ingredients to the dish instance
            for ingredient in new_ingredients:
                if ingredient not in existing_ingredients:
                    instance.ingredients.add(ingredient)

        return instance

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['name', 'image', 'parent', 'restaurant']
        extra_kwargs = {'id': {'write_only': True}, 'image': {'write_only': True}, 'parent': {'write_only': True}}

class SubMenuSerializer(serializers.ModelSerializer):
    dishes = DishSerializer(many=True)
    class Meta:
        model = Menu
        fields = ['name', 'image', 'parent', 'restaurant', 'dishes']
        extra_kwargs = {'id': {'write_only': True}, 'parent': {'write_only': True}, 'restaurant': {'write_only': True}}
