from django.db import models

# Third-party imports
import uuid


class BaseModel(models.Model):
    """
    Base model for all models in the application.
    Provides an UUID primary key, created and updated timestamps.
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
        return f"{self.__class__.__name__}({self.id})"

    @classmethod
    def get_model_name(cls):
        """
        Returns the model name.
        """
        return cls.__name__
