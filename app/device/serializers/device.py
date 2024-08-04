from device.models import Device
from rest_framework import serializers


class DeviceSerializer(serializers.ModelSerializer):
    distance = serializers.FloatField(read_only=True)

    class Meta:
        model = Device
        fields = [
            'id',
            'user',
            'name',
            'identifier',
            'front_photo',
            'side_photo',
            'status',
            'longitude',
            'latitude',
            'created_at',
            'updated_at',
            'distance'
        ]

        read_only_fields = ['id', 'status',
                            'created_at', 'updated_at', 'distance']
