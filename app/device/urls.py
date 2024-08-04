from django.urls import path, include
from rest_framework.routers import DefaultRouter
from device.views import DeviceViewSet, DeviceConfigurationViewSet, DeviceDataViewSet

router = DefaultRouter()
router.register(r'devices', DeviceViewSet)
router.register(r'device-configurations', DeviceConfigurationViewSet)
router.register(r'device-data', DeviceDataViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
