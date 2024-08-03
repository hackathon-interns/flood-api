from device.models import DeviceConfiguration
from rest_framework import serializers


class DeviceConfigurationSerializer(serializers.ModelSerializer):

    class Meta:
        model = DeviceConfiguration
        fields = [
            'device',
            'calibration_offset',
            'calibration_scale',
            'normal_water_level',
            'alert_water_level',
            'danger_water_level',
            'rainfall_threshold'
        ]
