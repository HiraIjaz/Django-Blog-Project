"""
Django admin configuration for CustomUser model.

This module defines the admin interface configuration for the CustomUser model,
providing custom display options, fieldsets, and search functionality.

"""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    """
    Admin class for CustomUser model.

    This class defines the configuration for the admin interface of the CustomUser model,
    including display options, fieldsets, and search functionality.

    Attributes:
        model (CustomUser): The CustomUser model to be administered.
        list_display (tuple): Fields to be displayed in the list view.
        list_filter (tuple): Fields by which the list view can be filtered.
        fieldsets (tuple): Groupings of fields in the detail view.
        add_fieldsets (tuple): Groupings of fields in the add view.
        search_fields (tuple): Fields to be searched in the admin interface.
        ordering (tuple): Default ordering for the list view.

    """

    model = CustomUser
    list_display = ('phone', 'is_staff', 'is_active',)
    list_filter = ('phone', 'is_staff', 'is_active',)
    fieldsets = (
        ('Basic Info', {'fields': ('phone', 'password')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Personal Info', {'fields': ('email', 'name', 'gender')})
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'phone', 'password1', 'password2', 'name', 'email', 'gender', 'is_staff',
                'is_active', 'groups', 'user_permissions',
            )}
         ),
    )
    search_fields = ('phone', 'name')
    ordering = ('phone',)


# Register the CustomUser model with the CustomUserAdmin configuration
admin.site.register(CustomUser, CustomUserAdmin)
