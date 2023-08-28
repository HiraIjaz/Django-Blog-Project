from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    """
    Custom manager for the CustomUser model.
    """

    def create_user(self, phone, password, **extra_fields):
        """
        Creates and saves a regular user with the given phone and password.

        Args:
            phone (str): The user's phone number.
            password (str): The user's password.
            **extra_fields: Additional fields to be saved for the user.

        Returns:
            CustomUser: The created user instance.

        Raises:
            ValueError: If the phone number is not provided.
        """
        if not phone:
            raise ValueError('Phonenumber required!')
        extra_fields['email'] = self.normalize_email(extra_fields['email'])
        user = self.model(phone=phone, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, phone, password, **extra_fields):
        """
        Creates and saves a superuser with the given phone and password.

        Args:
            phone (str): The superuser's phone number.
            password (str): The superuser's password.
            **extra_fields: Additional fields to be saved for the superuser.

        Returns:
            CustomUser: The created superuser instance.

        Raises:
            ValueError: If is_staff or is_superuser is not set to True.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        extra_fields['email'] = phone + 'gmail.com'

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(phone, password, **extra_fields)
