from device.models import DeviceConfiguration
from django.contrib import admin
from core.admin import AdminBase


@admin.register(DeviceConfiguration)
class DeviceConfigurationAdmin(AdminBase):
    list_display = [
        'device',
        'danger_water_level',
        'alert_water_level'
    ]

    search_fields = [
        'device__code',
        'device__user__email',
        'device__user__first_name',
        'device__user__last_name'
    ]
