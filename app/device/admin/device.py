from device.models import Device
from django.contrib import admin
from core.admin import AdminBase

@admin.register(Device)
class DeviceAdmin(AdminBase):
    list_display = [
        'user',
        'code',
        'status',
        'longitude',
        'latitude'
    ]

    search_fields = [
        'code',
        'user__email',
        'user__first_name',
        'user__last_name'
    ]

    list_filter = [
        'status'
    ]
