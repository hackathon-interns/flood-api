from django.urls import path, include
from rest_framework.routers import DefaultRouter
from device.views import DeviceViewSet
from device.views import DeviceConfigurationViewSet

router = DefaultRouter()
router.register(r'devices', DeviceViewSet)
router.register(r'device_configurations', DeviceConfigurationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
