from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from debug_toolbar.toolbar import debug_toolbar_urls
from user.views import UserViewSet
from lunchroom.views import RestaurantViewSet, MenuViewSet, SubMenuViewSet, DishViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'restaurants', RestaurantViewSet, basename='restaurant')
router.register(r'menus', MenuViewSet, basename='menu')
router.register(r'submenus', SubMenuViewSet, basename='submenu')
router.register(r'dishes', DishViewSet, basename='dish')

urlpatterns = [
    path('admin/', admin.site.urls),
    path("i18n/", include("django.conf.urls.i18n")),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest-framework'))
] + debug_toolbar_urls()
