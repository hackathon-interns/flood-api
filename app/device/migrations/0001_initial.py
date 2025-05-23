# Generated by Django 5.0.7 on 2024-08-04 15:05

import django.core.validators
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True, verbose_name='Identificador')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('name', models.CharField(max_length=255, verbose_name='Nome do Dispositivo')),
                ('identifier', models.CharField(help_text='Identificador único do dispositivo', max_length=255, unique=True, verbose_name='Identificador do Dispositivo')),
                ('front_photo', models.ImageField(upload_to='device_photos/', verbose_name='Foto Frontal')),
                ('side_photo', models.ImageField(upload_to='device_photos/', verbose_name='Foto Lateral')),
                ('status', models.CharField(choices=[('ACTIVE', 'Ativo'), ('INACTIVE', 'Inativo'), ('UNVERIFIED', 'Não Verificado')], default='UNVERIFIED', max_length=20, verbose_name='Status do Dispositivo')),
                ('longitude', models.FloatField(help_text='Entre -180 e 180', validators=[django.core.validators.MinValueValidator(-180.0), django.core.validators.MaxValueValidator(180.0)], verbose_name='Longitude')),
                ('latitude', models.FloatField(help_text='Entre -90 e 90', validators=[django.core.validators.MinValueValidator(-90.0), django.core.validators.MaxValueValidator(90.0)], verbose_name='Latitude')),
            ],
            options={
                'verbose_name': 'Dispositivo',
                'verbose_name_plural': 'Dispositivos',
            },
        ),
        migrations.CreateModel(
            name='DeviceConfiguration',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True, verbose_name='Identificador')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('calibration_offset', models.DecimalField(decimal_places=3, help_text='cm', max_digits=12, verbose_name='Taxa de Erro')),
                ('calibration_scale', models.DecimalField(decimal_places=3, help_text='para cm', max_digits=12, verbose_name='Conversão da Unidade de Medida')),
                ('normal_water_level', models.DecimalField(decimal_places=3, help_text='cm', max_digits=12, verbose_name='Nível de Água Normal')),
                ('alert_water_level', models.DecimalField(decimal_places=3, help_text='cm', max_digits=12, verbose_name='Nível de Água de Alerta')),
                ('danger_water_level', models.DecimalField(decimal_places=3, help_text='cm', max_digits=12, verbose_name='Nível de Água de Perigo')),
                ('rainfall_threshold', models.DecimalField(decimal_places=3, help_text='mm', max_digits=12, verbose_name='Limite de Precipitação')),
                ('data_mapping', models.JSONField(verbose_name='Mapeamento de Dados')),
            ],
            options={
                'verbose_name': 'Configuração do Dispositivo',
                'verbose_name_plural': 'Configurações dos Dispositivos',
            },
        ),
        migrations.CreateModel(
            name='DeviceData',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True, verbose_name='Identificador')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('distance_to_water', models.DecimalField(decimal_places=3, help_text='cm', max_digits=12, verbose_name='Distancia da Água')),
                ('pluviometer_value', models.DecimalField(decimal_places=3, help_text='mm', max_digits=12, verbose_name='Nível de Água')),
            ],
            options={
                'verbose_name': 'Dado do Dispositivo',
                'verbose_name_plural': 'Dados dos Dispositivos',
            },
        ),
    ]
