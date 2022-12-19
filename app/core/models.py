"""
    Database models
"""

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
