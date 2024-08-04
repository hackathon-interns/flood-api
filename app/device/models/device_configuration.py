from django.db import models
from core.models import BaseModel


class DeviceConfiguration(BaseModel):
    device = models.OneToOneField(
        'device.Device',
        on_delete=models.CASCADE,
        related_name='configuration'
    )

    calibration_offset = models.DecimalField(
        max_digits=12,
        decimal_places=3,
        verbose_name="Taxa de Erro",
        help_text="cm"
    )

    calibration_scale = models.DecimalField(
        max_digits=12,
        decimal_places=3,
        verbose_name="Conversão da Unidade de Medida",
        help_text="para cm"
    )

    normal_water_level = models.DecimalField(
        max_digits=12,
        decimal_places=3,
        verbose_name="Nível de Água Normal",
        help_text="cm"
    )

    alert_water_level = models.DecimalField(
        max_digits=12,
        decimal_places=3,
        verbose_name="Nível de Água de Alerta",
        help_text="cm"
    )

    danger_water_level = models.DecimalField(
        max_digits=12,
        decimal_places=3,
        verbose_name="Nível de Água de Perigo",
        help_text="cm"
    )

    rainfall_threshold = models.DecimalField(
        max_digits=12,
        decimal_places=3,
        verbose_name="Limite de Precipitação",
        help_text="mm"
    )
    data_mapping = models.JSONField(verbose_name="Mapeamento de Dados")

    class Meta:
        verbose_name = "Configuração do Dispositivo"
        verbose_name_plural = "Configurações dos Dispositivos"

    def save(self, *args, **kwargs):
        """
        Save the device configuration.
        """
        if not self.device.status == 'UNVERIFIED':
            self.device.status = 'ACTIVE'
            self.device.save()
        super().save(*args, **kwargs)
