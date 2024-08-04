from device.models import DeviceData
from rest_framework import serializers


class DeviceDataSerializer(serializers.ModelSerializer):
    status = serializers.SerializerMethodField()

    class Meta:
        model = DeviceData
        fields = [
            'id',
            'device',
            'distance_to_water',
            'pluviometer_value',
            'created_at',
            'updated_at',
            'status'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at', 'status']

    def get_status(self, obj):
        configuration = obj.device.configuration
        if obj.distance_to_water <= configuration.alert_water_level:
            return 'warning'
        if obj.distance_to_water <= configuration.danger_water_level:
            return 'danger'
        return 'normal'
