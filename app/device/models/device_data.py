from django.db import models
from core.models import BaseModel


class DeviceData(BaseModel):
    device = models.ForeignKey(
        'device.Device',
        on_delete=models.CASCADE,
        related_name='data'
    )

    distance_to_water = models.DecimalField(
        max_digits=12,
        decimal_places=3,
        verbose_name="Distancia da Água",
        help_text="cm"
    )

    pluviometer_value = models.DecimalField(
        max_digits=12,
        decimal_places=3,
        verbose_name="Nível de Água",
        help_text="mm"
    )

    class Meta:
        verbose_name = "Dado do Dispositivo"
        verbose_name_plural = "Dados dos Dispositivos"
