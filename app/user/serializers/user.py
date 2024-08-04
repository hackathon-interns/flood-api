from user.models import User
from rest_framework import serializers
from django.conf import settings


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    profile_img_url = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email', 'profile_img',
                  'notify_on_new_station', 'stations_to_notify', 'profile_img_url']
        read_only_fields = ['stations_to_notify', 'id', 'profile_img_url']
        optional_fields = ['profile_img', 'notify_on_new_station']

    def get_profile_img_url(self, obj):
        print(obj.profile_img)
        if obj.profile_img:
            return 'http://192.168.1.100:8080' + obj.profile_img.url
        return None

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email']
        )
        return user
