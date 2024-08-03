from django.db import models
from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser,
    PermissionsMixin
)
from django.core.validators import MinLengthValidator
from core.models import BaseModel


class UserManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        """
        Creates and saves a User with the given email, username and password.
        """
        if not email:
            raise ValueError("Usuários devem ter um endereço de e-mail")

        if not username:
            raise ValueError("Usuários devem ter um nome de usuário")

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
            username=username,
        )
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin, BaseModel):
    """
    Custom user model with email as the unique identifier
    """
    email = models.EmailField(
        verbose_name="Endereço de e-mail",
        max_length=255,
        unique=True,
    )
    username = models.CharField(
        verbose_name="Nome de usuário",
        max_length=255,
        validators=[MinLengthValidator(3)],
        unique=True
    )
    profile_img = models.ImageField(
        upload_to='profile_images/', null=True, blank=True)
    stations_to_notify = models.ManyToManyField(
        'device.Device',
        related_name='notified_users',
        blank=True
    )

    notify_on_new_station = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        """
        String representation of the user
        """
        return self.email

    @property
    def is_superuser(self):
        """
        Is the user a superuser?
        """
        return self.is_staff
