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

    user = models.ForeignKey(
        'user.User',
        on_delete=models.CASCADE,
        related_name='devices'
    )

    code = models.CharField(
        max_length=255,
        unique=True
    )

    front_photo = models.ImageField(upload_to='device_photos/')
    side_photo = models.ImageField(upload_to='device_photos/')

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='UNVERIFIED'
    )

    longitude = models.FloatField(
        validators=[
            MinValueValidator(-180.0),
            MaxValueValidator(180.0)
        ]
    )

    latitude = models.FloatField(
        validators=[
            MinValueValidator(-90.0),
            MaxValueValidator(90.0)
        ]
    )
