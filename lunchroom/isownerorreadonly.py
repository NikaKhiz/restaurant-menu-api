from rest_framework import permissions
from .models import Restaurant, Menu, Dish


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        if  not request.user or not request.user.is_authenticated:
            return False
            
        if view.basename == 'restaurant':
            return True
        
        if view.basename == 'menu':
            restaurant = request.data.get('restaurant')
            if restaurant and Restaurant.objects.get(id=restaurant).user == request.user:
                return True
            return True
        if view.basename == 'submenu':
            menu_id = request.data.get('parent')
            if menu_id and Menu.objects.get(id=menu_id).restaurant.user == request.user:
                return True
            return False
        if view.basename == 'dish':
            menu_id = request.data.get('menu')
            if menu_id and Menu.objects.get(id=menu_id).restaurant.user == request.user:
                return True
            return False

        return False

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        if isinstance(obj, Restaurant):
            return obj.user == request.user

        if isinstance(obj, Menu):
            return obj.restaurant.user == request.user

        if isinstance(obj, Dish):
            return obj.menu.restaurant.user == request.user

        return False
