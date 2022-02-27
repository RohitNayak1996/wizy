from django.db import models
from django.contrib.auth.models import  AbstractUser,PermissionsMixin

from usermanagement.managers import CustomUserManager


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    objects = CustomUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    def __str__(self):
        return self.email

class Movies(models.Model):
    movie = models.CharField(max_length=200)
    def __str__(self):
        return self.movie