from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.exceptions import PermissionDenied
from device.models import DeviceConfiguration
from device.serializers import DeviceConfigurationSerializer


class DeviceConfigurationViewSet(viewsets.ModelViewSet):
    queryset = DeviceConfiguration.objects.all()
    serializer_class = DeviceConfigurationSerializer
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]

    def update(self, request, *args, **kwargs):
        device_configuration = self.get_object()
        if request.user != device_configuration.device.user:
            raise PermissionDenied(
                "Você não tem permissão para atualizar este as configuracoes desse dispositivo.")
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        raise PermissionDenied(
            "Nao e possivel apagar as configuracoes de um dispositivo.")
