from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from device.models import Device
from device.serializers import DeviceSerializer
from rest_framework.decorators import action


class DeviceViewSet(viewsets.ModelViewSet):
    '''
    ViewSet for the `Device` model.

    This ViewSet provides CRUD operations for the `Device` model, including update and delete operations. 
    Additionally, it allows users to add devices to their notification list.
    '''
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        """
        Update an existing device.

        Checks if the authenticated user is the owner of the device before allowing the update.
        """
        device = self.get_object()
        if request.user != device.user:
            raise PermissionDenied(
                "Você não tem permissão para atualizar este dispositivo.")
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        """
        Deactivate a device instead of deleting it.

        Sets the device's status to 'INACTIVE' rather than removing it from the database.
        """
        device = self.get_object()
        device.status = "INACTIVE"
        device.save()

        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=True, methods=['post'])
    def add_to_notifications(self, request, pk=None):
        """
        Add a device to the user's notification list.

        Adds the device to the user's list of stations to notify when the device's data indicates a dangerous water level.
        """
        device = self.get_object()
        user = request.user

        if device.status != "ACTIVE":
            return Response({"detail": "O dispositivo não está ativo."}, status=status.HTTP_400_BAD_REQUEST)

        if device in user.stations_to_notify.all():
            return Response({"detail": "O dispositivo já está na lista de notificações."}, status=status.HTTP_400_BAD_REQUEST)

        user.stations_to_notify.add(device)
        return Response({"detail": "Dispositivo adicionado à lista de notificações."}, status=status.HTTP_200_OK)
