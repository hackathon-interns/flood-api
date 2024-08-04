from django.contrib import admin
from core.admin import AdminBase
from user.models import User


@admin.register(User)
class Userdmin(AdminBase):
    list_display = [
        'email',
        'username',
        'is_active',
        'is_staff'
    ]

    search_fields = [
        'email',
        'first_name',
        'last_name'
    ]

    list_filter = [
        'is_active',
        'is_staff'
    ]
