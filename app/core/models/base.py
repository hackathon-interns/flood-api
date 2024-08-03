from django.db import models
import uuid


class BaseModel(models.Model):
    """
    Base model for all models in the application
    """
    id = models.UUIDField(
        default=uuid.uuid4, editable=False, unique=True, primary_key=True, verbose_name='Identificador')
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name='Atualizado em')

    class Meta:
        abstract = True
        ordering = ['-created_at']

    def __str__(self):
        return str(self.id)
