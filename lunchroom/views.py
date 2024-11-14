from rest_framework import status, viewsets, permissions
from .models import Restaurant, Menu
from .serializers import RestaurantSerializer, MenuSerializer, SubMenuSerializer
from django_filters import rest_framework as filters

class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.filter(parent__isnull=True)
    serializer_class = MenuSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class SubMenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.filter(parent__isnull=False)
    serializer_class = SubMenuSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filterset_fields = ('parent', 'dishes')

