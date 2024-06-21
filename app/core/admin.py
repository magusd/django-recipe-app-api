from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from core import models
from django.utils.translation import gettext_lazy as _

class UserAdmin(BaseUserAdmin):
    """Define admin model for User model."""
    ordering = ['id']
    list_display = ['email', 'name']
    fieldsets = (
        (None,
            {'fields': ('email', 'password')}),
        (_('Permissions'),
            {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        (_('Important dates'),
            {'fields': ('last_login',)}),
        (_('Personal info'),
            {'fields': ('name',)}),
    )
    readonly_fields = ['last_login', 'is_superuser', 'is_staff']

    add_fieldsets = [
        (None,
         {'fields': ('email',
                               'password1',
                               'password2',
                               'name',
                               'is_active',
                               'is_staff',
                               'is_superuser',
                     )}),
    ]
    # exclude = ['username','first_name', 'last_name', 'date_joined']


admin.site.register(models.User, UserAdmin)
