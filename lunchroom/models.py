from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from versatileimagefield.fields import VersatileImageField
from django.utils.translation import gettext_lazy as _


class Restaurant(models.Model):
    name = models.CharField(max_length=40, unique=True, null=False, blank=False, verbose_name=_('name'))
    address = models.CharField(max_length=150, unique=True, null=False, blank=False, verbose_name=_('address'))
    phone_number = models.CharField(max_length=15, unique=True, blank=False, null=False, verbose_name=_('phone_number'))
    image = VersatileImageField(upload_to='restaurant/', null=True, blank=True, verbose_name=_('image'))

    class Meta:
        verbose_name = _("restaurant")
        verbose_name_plural = _('restaurants')
        
    def __str__(self):
        return self.name

class Menu(MPTTModel):
    name = models.CharField(max_length=40, unique=True, null=False, blank=False, verbose_name=_('name'))
    parent = TreeForeignKey('self', null=True, blank=True, related_name='subcategories', on_delete=models.CASCADE, verbose_name=_('parent'))
    restaurant = models.ForeignKey('lunchroom.Restaurant', related_name='menu', null=False, blank=False, on_delete=models.CASCADE, verbose_name=_('restaurant'))
    image = VersatileImageField(upload_to='menu_category/', null=True, blank=True, verbose_name=_('image'))

    class Meta:
        verbose_name = _("menu")
        verbose_name_plural = _('menues')
        
    def __str__(self):
        return self.name


class Dish(models.Model):
    name = models.CharField(max_length=255, unique=True, blank=False, null=False, verbose_name=_('name'))
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name=_('price'))
    menu = models.ForeignKey('lunchroom.Menu', related_name='dishes', on_delete=models.CASCADE, verbose_name=_('menu'))
    image = VersatileImageField(upload_to='dish/', null=True, blank=True, verbose_name=_('image'))
    
    class Meta:
        verbose_name = _("dish")
        verbose_name_plural = _('dishes')
        
    def __str__(self):
        return self.name
    

class Ingredient(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False, verbose_name=_('name'))
    dish = models.ManyToManyField('lunchroom.Dish', related_name='ingredients', verbose_name=_('dish'))
    
    class Meta:
        verbose_name = _("ingredient")
        verbose_name_plural = _('ingredients')
        
    def __str__(self):
        return self.name