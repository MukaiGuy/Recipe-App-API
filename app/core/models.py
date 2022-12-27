"""
    Database models
"""
from django.conf import settings
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)


class UserManager(BaseUserManager):
    # Manager for users

    def create_user(self, email, password=None, **extra_field):
        # Create, Save, and return a new user
        if not email:
            raise ValueError("Please provide an email address")

        user = self.model(email=self.normalize_email(email), **extra_field)
        # **extra_field can provide nay number of keyword arguments
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        # Create and return a new superuser
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    # User in the system
    email = models.EmailField(
        ("Email"), max_length=254, unique=True)
    firstname = models.CharField(("First Name"), max_length=255)
    lastname = models.CharField(("Last Name"), max_length=255)
    is_active = models.BooleanField(("Is Active"), default=True)
    is_staff = models.BooleanField(("Is Staff"), default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'


class Recipe(models.Model):
    """ Recipe Object """
    user = models.ForeignKey(
        # Referance the settings to prevent hard coding the user model
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    title = models.CharField(("Title"), max_length=255)
    description = models.TextField(("Description"), blank=True)
    time_minutes = models.IntegerField(("Time (mins)"),)
    price = models.DecimalField(("Price"), max_digits=5, decimal_places=2)
    link = models.CharField(("Link"), max_length=255, blank=True)

    def __str__(self):
        """ This method returns the string representation of the object. """
        return self.title
