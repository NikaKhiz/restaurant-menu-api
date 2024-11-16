from rest_framework import  viewsets, permissions
from .models import Restaurant, Menu, Dish
from .serializers import RestaurantSerializer, MenuSerializer, SubMenuSerializer, DishSerializer

class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.filter(parent__isnull=True)
    serializer_class = MenuSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class SubMenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.filter(parent__isnull=False).prefetch_related('dishes__ingredients')
    serializer_class = SubMenuSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filterset_fields = ('parent', 'dishes')


class DishViewSet(viewsets.ModelViewSet):
    queryset = Dish.objects.prefetch_related('ingredients')
    serializer_class = DishSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filterset_fields = ('name',)