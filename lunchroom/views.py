from rest_framework import  viewsets, permissions
from .models import Restaurant, Menu, Dish
from .serializers import RestaurantSerializer, MenuSerializer, SubMenuSerializer, DishSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.filter(parent__isnull=True)
    serializer_class = MenuSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class SubMenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.filter(parent__isnull=False).prefetch_related('dishes')
    serializer_class = SubMenuSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filterset_fields = ('parent', 'dishes')


    @action(detail=True, methods=['get'])
    def get_dishes(self, request, pk=None):
        submenu = Menu.objects.filter(id=pk).first()
        dishes = submenu.dishes.all() 
        return Response(DishSerializer(dishes, many=True).data)
    
class DishViewSet(viewsets.ModelViewSet):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filterset_fields = ('name',)