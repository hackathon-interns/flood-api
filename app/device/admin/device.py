from device.models import Device
from django.contrib import admin
from core.admin import AdminBase


@admin.register(Device)
class DeviceAdmin(AdminBase):
    list_display = [
        'name',
        'user',
        'identifier',
        'status',
        'longitude',
        'latitude'
    ]

    search_fields = [
        'user__email',
        'user__first_name',
        'user__last_name'
    ]

    list_filter = [
        'status'
    ]
