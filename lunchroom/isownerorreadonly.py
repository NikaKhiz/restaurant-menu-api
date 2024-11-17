from rest_framework import permissions
from .models import Restaurant, Menu, Dish


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        if  request.user and request.user.is_authenticated:
            if view.basename == 'restaurant':
                return True

            if view.basename == 'menu':
                restaurant = request.data.get('restaurant')
                if restaurant is not None:
                    if restaurant and Restaurant.objects.get(id=restaurant).user == request.user:
                        return True
                    else:
                        return False
                else:
                    return True
                
            if view.basename == 'submenu':
                menu_id = request.data.get('parent')
                if menu_id is not None:
                    if menu_id and Menu.objects.get(id=menu_id).restaurant.user == request.user:
                        return True
                    else:
                        return False
                else:
                    return True
                
            if view.basename == 'dish':
                menu_id = request.data.get('menu')
                if menu_id is not None:

                    if menu_id and Menu.objects.get(id=menu_id).restaurant.user == request.user:
                        return True
                    else:
                        return False
                else:
                    return True

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
