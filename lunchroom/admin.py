from django.contrib import admin
from .models import Restaurant,Menu,Dish,Ingredient
from django.utils.translation import gettext_lazy as _
from modeltranslation.admin import TabbedTranslationAdmin
from admin_auto_filters.filters import AutocompleteFilter

@admin.register(Restaurant)
class RestaurantAdmin(TabbedTranslationAdmin):
    list_display = ('name', 'address', 'phone_number')
    search_fields = ('name',)
    list_filter = ['name', 'address']
    ordering = ('name',)
    list_editable = ('address', 'phone_number')


class MenuFilter(AutocompleteFilter):
    title = 'Menu' 
    field_name = 'parent' 

@admin.register(Menu)
class MenuAdmin(TabbedTranslationAdmin):
    list_display = ('name', 'parent', 'restaurant')
    search_fields = ('name',)
    list_filter = [MenuFilter , 'name', 'restaurant']
    ordering = ('name',)
    list_editable = ('parent', 'restaurant')


@admin.register(Dish)
class DishAdmin(TabbedTranslationAdmin):
    list_display = ('name', 'menu', 'price')
    search_fields = ('name',)
    list_filter = ['name', 'menu', 'price']
    ordering = ('name',)
    list_editable = ('menu', 'price')


@admin.register(Ingredient)
class IngredientAdmin(TabbedTranslationAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    list_filter = ['name',]
    ordering = ('name',)
