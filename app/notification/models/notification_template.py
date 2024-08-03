from django.db import models
from core.models import BaseModels


class NotificationTemplate(BaseModels):
    '''
    Model to store the notification templates
    '''
    title = models.CharField(max_length=150)
    template = models.TextField()
