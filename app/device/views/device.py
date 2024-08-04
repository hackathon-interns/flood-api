from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.exceptions import PermissionDenied
from device.models import Device
from device.serializers import DeviceSerializer, DeviceDataSerializer, DeviceConfigurationSerializer
from rest_framework.decorators import action


class DeviceViewSet(viewsets.ModelViewSet):
    '''
    ViewSet for the Device model.

    This ViewSet provides CRUD operations for the `Device` model, including update and delete operations. 
    Additionally, it allows users to add devices to their notification list.
    '''
    queryset = Device.objects.filter(status="ACTIVE")
    serializer_class = DeviceSerializer
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

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

    @action(detail=True, methods=['post'])
    def remove_from_notifications(self, request, pk=None):
        """
        Remove a device from the user's notification list.

        Removes the device from the user's list of stations to notify when the device's data indicates a dangerous water level.
        """
        device = self.get_object()
        user = request.user

        if device not in user.stations_to_notify.all():
            return Response({"detail": "O dispositivo não está na lista de notificações."}, status=status.HTTP_400_BAD_REQUEST)

        user.stations_to_notify.remove(device)
        return Response({"detail": "Dispositivo removido da lista de notificações."}, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'])
    def list_notifications(self, request):
        """
        List the devices in the user's notification list.

        Returns a list of devices that the user has added to their notification list.
        """

        # mock latitude and longitude for testing
        # lat = -23.5505199
        # long = -46.6333094
        user = request.user
        devices = user.stations_to_notify.all()
        lat = request.query_params.get('latitude')
        long = request.query_params.get('longitude')

        if lat and long:
            for device in devices:
                setattr(device, 'distance',
                        device.calculate_distance(lat, long))
        serializer = DeviceSerializer(devices, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=['get'])
    def latest_data(self, request, pk=None):
        """
        Retrieve the latest data from a device.

        Returns the latest data entry for the specified device.
        """
        device = self.get_object()
        try:
            latest_data = device.data.order_by('-created_at').first()
            serializer = DeviceDataSerializer(latest_data)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Device.DoesNotExist:
            return Response({"detail": "Este dispositivo não possui dados associados."}, status=status.HTTP_404_NOT_FOUND)

    @action(detail=True, methods=['get'])
    def configuration(self, request, pk=None):
        """
        Retrieve the configuration for a device.

        Returns the configuration for the specified device.
        """
        device = self.get_object()
        try:
            configuration = device.configuration
            serializer = DeviceConfigurationSerializer(configuration)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Device.DoesNotExist:
            return Response({"detail": "Este dispositivo não possui configurações associadas."}, status=status.HTTP_404_NOT_FOUND)
