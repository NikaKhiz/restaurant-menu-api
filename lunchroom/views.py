from rest_framework import  viewsets, permissions
from .models import Restaurant, Menu, Dish
from .serializers import RestaurantSerializer, MenuSerializer, SubMenuSerializer, DishSerializer
from .isownerorreadonly import IsOwnerOrReadOnly

class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.filter(parent__isnull=True)
    serializer_class = MenuSerializer
    permission_classes = [IsOwnerOrReadOnly]


class SubMenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.filter(parent__isnull=False).prefetch_related('dishes__ingredients')
    serializer_class = SubMenuSerializer
    permission_classes = [IsOwnerOrReadOnly]
    filterset_fields = ('parent', 'dishes')


class DishViewSet(viewsets.ModelViewSet):
    queryset = Dish.objects.prefetch_related('ingredients')
    serializer_class = DishSerializer
    permission_classes = [IsOwnerOrReadOnly]
    filterset_fields = ('name','menu')