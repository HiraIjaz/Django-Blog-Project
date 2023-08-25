from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    # add_form = CustomUserCreationForm
    # form = CustomUserChangeForm
    model = CustomUser
    list_display = ("phone", "is_staff", "is_active",)
    list_filter = ("phone", "is_staff", "is_active",)
    fieldsets = (
        ('Basic Info', {'fields': ('phone', 'password')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Personal Info', {'fields': ('email', 'name', 'gender')})
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "phone", "password1", "password2", 'name', 'email', 'gender', "is_staff",
                "is_active", "groups", "user_permissions",
            )}
         ),
    )
    search_fields = ("phone",)
    ordering = ("phone",)


admin.site.register(CustomUser, CustomUserAdmin)
