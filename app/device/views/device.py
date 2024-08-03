from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from device.models import Device
from device.serializers import DeviceSerializer


class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        device = self.get_object()
        if request.user != device.user:
            raise PermissionDenied(
                "Você não tem permissão para atualizar este dispositivo.")
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        device = self.get_object()
        device.status = "INACTIVE"
        device.save()

        return Response(status=status.HTTP_204_NO_CONTENT)
