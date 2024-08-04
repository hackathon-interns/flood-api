from rest_framework import viewsets, status, response
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.exceptions import PermissionDenied
from device.models import Device, DeviceData
from device.serializers import DeviceDataSerializer
from rest_framework.decorators import action


def map_data(data, mapping):
    """
    Map data based on the provided mapping. Handles nested structures, arrays, and key-value pairs.

    Parameters:
    - data: The input data to map.
    - mapping: A dictionary where keys are the desired output keys and values are lists of possible input keys.

    Returns:
    - A dictionary with the mapped data.
    """
    def extract_value(data, possible_keys):
        """Recursively search for a value in the data based on possible_keys."""
        if not isinstance(data, (dict, list)):
            return None

        # Check if data is a dictionary
        if isinstance(data, dict):
            for key in possible_keys:
                if key in data:
                    return data[key]

            # Check nested dictionaries
            for k, v in data.items():
                if isinstance(v, dict):
                    result = extract_value(v, possible_keys)
                    if result is not None:
                        return result

            # Check arrays of dictionaries
            for k, v in data.items():
                if isinstance(v, list):
                    result = extract_value(v, possible_keys)
                    if result is not None:
                        return result

        # Check if data is a list of dictionaries
        elif isinstance(data, list):
            for item in data:
                if isinstance(item, dict):
                    # Check for direct match in the list items
                    result = extract_value(item, possible_keys)
                    if result is not None:
                        return result

                    # Check for type-based extraction
                    if 'type' in item and 'value' in item:
                        if item['type'] in possible_keys:
                            return item['value']

        return None

    mapped_data = {}
    for standard_key, possible_keys in mapping.items():
        value = extract_value(data, possible_keys)
        mapped_data[standard_key] = value

    return mapped_data


class DeviceDataViewSet(viewsets.ModelViewSet):
    queryset = DeviceData.objects.all()
    serializer_class = DeviceDataSerializer
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]

    def update(self, request, *args, **kwargs):
        device_data = self.get_object()
        if request.user != device_data.device.user:
            raise PermissionDenied(
                "Você não tem permissão para atualizar os dados desse dispositivo.")

        raw_data = request.data.get('data', {})
        mapped_data = map_data(raw_data, device_data.device.data_mapping)

        if mapped_data['identifier'] != device_data.device.identifier:
            raise PermissionDenied(
                "O código do dispositivo não corresponde ao código do dispositivo associado.")

        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        raise PermissionDenied(
            "Nao e possivel apagar os dados de um dispositivo.")

    def create(self, request, *args, **kwargs):
        device_id = request.data.get('identifier', None)

        try:
            device = Device.objects.get(identifier=device_id)
            # if device.user != request.user:
            #     raise PermissionDenied(
            #         "Você não tem permissão para adicionar dados a esse dispositivo.")
            if not hasattr(device, 'configuration') or not device.configuration:
                raise PermissionDenied(
                    "Este dispositivo não possui configurações associadas.")
        except Device.DoesNotExist:
            raise PermissionDenied(
                "Este dispositivo não existe ou não está associado ao seu usuário.")

        mapped_data = map_data(request.data, device.configuration.data_mapping)
        if not mapped_data:
            raise PermissionDenied(
                "Os dados fornecidos não correspondem ao mapeamento de dados do dispositivo.")

        serializer = DeviceDataSerializer(
            data={**mapped_data, 'device': device.id})
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
