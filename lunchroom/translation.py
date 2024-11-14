from modeltranslation.translator import register, TranslationOptions
from .models import Dish, Ingredient, Menu, Restaurant

class BaseTranslationOptions(TranslationOptions):
    fields = ('name',)
    required_languages = ('en', 'ka')

@register(Restaurant)
class RestaurantTranslationOptions(BaseTranslationOptions):
    fields = ('address',)
    


@register(Menu)
class MenuTranslationOptions(BaseTranslationOptions):
    pass


@register(Dish)
class DishTranslationOptions(BaseTranslationOptions):
    pass


@register(Ingredient)
class IngredientTranslationOptions(BaseTranslationOptions):
    pass

