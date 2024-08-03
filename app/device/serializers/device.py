from device.models import Device
from rest_framework import serializers


class DeviceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Device
        fields = [
            'user',
            'code',
            'front_photo',
            'side_photo',
            'status',
            'longitude',
            'latitude'
        ]

        read_only_fields = ['status']
