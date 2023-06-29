from django.contrib import admin
from django.contrib.admin import register

from user.models import User


@register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'email', 'username', 'first_name', 'last_name', 'is_active', 'is_admin']
