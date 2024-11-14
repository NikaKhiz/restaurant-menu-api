from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from debug_toolbar.toolbar import debug_toolbar_urls
from user.views import UserViewSet


router = routers.DefaultRouter()
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    path('admin/', admin.site.urls),
    path("i18n/", include("django.conf.urls.i18n")),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest-framework'))
] + debug_toolbar_urls()
