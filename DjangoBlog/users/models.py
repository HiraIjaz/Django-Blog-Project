from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager
from django.core.validators import MaxValueValidator, MinValueValidator


class CustomUser(AbstractUser):
    """
    Custom user model extending Django's AbstractUser.
    """
    # Choices for gender field
    GENDERS = [('M', 'Male'), ('F', 'Female'), ('O', 'Others')]
    # Custom fields
    username = None
    phone = models.CharField(
        _('phone'),
        max_length=11,
        unique=True,

    )
    email = models.EmailField(
        unique=True,

    )
    name = models.CharField(
        max_length=50,
        default='',

    )
    gender = models.CharField(
        max_length=1,
        choices=GENDERS,

    )
    age = models.PositiveIntegerField(
        blank=True,
        default=1,
        validators=[
            MinValueValidator(15),
            MaxValueValidator(70),
        ],
    )

    # Custom manager
    objects = CustomUserManager()

    # Set 'phone' as the username field
    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []

    def __str__(self):
        """
        Return a string representation of the user.
        """
        return self.name
