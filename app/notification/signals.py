from django.db.models.signals import post_save
from django.dispatch import receiver
from device.models import DeviceData, DeviceConfiguration
from django.core.mail import send_mail
from django.conf import settings


@receiver(post_save, sender=DeviceData)
def check_device_data(sender, instance, **kwargs):
    '''
    Check if the distance to water is in a dangerous level
    and send an email to the users to notify them.
    '''
    print(f"Checking data from device {instance.device.identifier}")
    config = DeviceConfiguration.objects.get(device=instance.device)

    if instance.distance_to_water <= config.danger_water_level:
        alert_level = "Perigo"
    elif instance.distance_to_water <= config.alert_water_level:
        alert_level = "Alerta"
    else:
        alert_level = "Normal"

    if alert_level != "Normal":
        users_to_notify = instance.device.notified_users.all()

        for user in users_to_notify:
            print(f"Sending notification to {user.email}")
