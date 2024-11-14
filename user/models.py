from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _




class CustomUser(AbstractUser):
    username=models.CharField(max_length=40,unique=True, verbose_name=_('username'))
    email=models.EmailField(max_length=255,unique=True, verbose_name=_('email'))

    def __str__(self):
        return self.username
