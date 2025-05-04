from django.db import models
from core.models import BaseModel
from django.core.validators import (
    MinValueValidator,
    MaxValueValidator
)


class Device(BaseModel):
    STATUS_CHOICES = [
        ('ACTIVE', 'Ativo'),
        ('INACTIVE', 'Inativo'),
        ('UNVERIFIED', 'Não Verificado'),
    ]

    name = models.CharField(max_length=255, verbose_name="Nome do Dispositivo")
    user = models.ForeignKey(
        'user.User',
        on_delete=models.CASCADE,
        related_name='devices',
        verbose_name="Usuário do Dispositivo"
    )

    identifier = models.CharField(
        max_length=255,
        unique=True,
        verbose_name="Identificador do Dispositivo",
        help_text="Identificador único do dispositivo"
    )

    front_photo = models.ImageField(
        upload_to='device_photos/', verbose_name="Foto Frontal", null=True, blank=True)
    side_photo = models.ImageField(
        upload_to='device_photos/', verbose_name="Foto Lateral", null=True, blank=True)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='UNVERIFIED',
        verbose_name="Status do Dispositivo"
    )

    longitude = models.FloatField(
        validators=[
            MinValueValidator(-180.0),
            MaxValueValidator(180.0)
        ],
        verbose_name="Longitude",
        help_text="Entre -180 e 180"
    )

    latitude = models.FloatField(
        validators=[
            MinValueValidator(-90.0),
            MaxValueValidator(90.0)
        ],
        verbose_name="Latitude",
        help_text="Entre -90 e 90"
    )

    def calculate_distance(self, latitude, longitude):
        """
        Calculate the distance between the device and given latitude and longitude.

        Returns the distance in kilometers.
        """
        from geopy.distance import geodesic

        device_location = (self.latitude, self.longitude)
        user_location = (latitude, longitude)

        return geodesic(device_location, user_location).kilometers

    def __str__(self):
        return f"{self.name} - {self.id}"

    class Meta:
        verbose_name = "Dispositivo"
        verbose_name_plural = "Dispositivos"
