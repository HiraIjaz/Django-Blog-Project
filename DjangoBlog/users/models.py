from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
GENDERS = [('M', 'Male'), ('F', 'Female'), ('O', 'Others')]


class CustomUser(AbstractUser):
    username = None
    phone = models.CharField(_("phone"), max_length=11, unique=True)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=50, default='')
    gender = models.CharField(max_length=1, choices=GENDERS)
    age = models.PositiveIntegerField(blank=True, default=1)
    USERNAME_FIELD = "phone"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.name


