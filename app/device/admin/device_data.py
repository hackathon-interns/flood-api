from device.models import DeviceData
from django.contrib import admin
from core.admin import AdminBase


@admin.register(DeviceData)
class DeviceDataAdmin(AdminBase):
    list_display = [
        'device',
        'distance_to_water',
        'pluviometer_value',
    ]

    search_fields = [
        'device__code',
        'device__user__email',
        'device__user__first_name',
        'device__user__last_name'
    ]

    list_filter = [
        'device__status'
    ]
