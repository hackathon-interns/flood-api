from django.db import models
from core.models import BaseModels


class Notifications(BaseModels):
    '''
    Model to store the notifications
    '''
    user = models.ForeignKey(
        'user.User',
        on_delete=models.CASCADE,
        related_name='notifications'
    )
    notification_template = models.ForeignKey('NotificationTemplate')
