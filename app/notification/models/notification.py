from django.db import models
from core.models import BaseModel


class Notifications(BaseModel):
    '''
    Model to store the notifications
    '''
    user = models.ForeignKey(
        'user.User',
        on_delete=models.CASCADE,
        related_name='notifications'
    )
    notification_template = models.ForeignKey(
        'notification.NotificationTemplate',
        on_delete=models.SET_NULL,
        related_name='notifications',
        blank=True,
        null=True
    )
