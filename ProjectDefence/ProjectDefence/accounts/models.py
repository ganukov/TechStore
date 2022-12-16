from ProjectDefence.accounts.managers import AppUserManager
from ProjectDefence.accounts.validators import check_name_contains_only_letters
from ProjectDefence.products.models import Product
from django.core.validators import MinValueValidator, MinLengthValidator, MaxLengthValidator

from django.db import models
from django.contrib.auth import models as auth_models

MIN_LENGTH_FIRST_NAME = 2
MAX_LENGTH_FIRST_NAME = 30
MIN_LENGTH_LAST_NAME = 2
MAX_LENGTH_LAST_NAME = 30
MIN_LENGTH_CITY_NAME = 5
MAX_LENGTH_CITY_NAME = 30
MIN_LENGTH_STREET_NAME = 5
MAX_LENGTH_STREET_NAME = 30
MIN_VALUE_NUMBER = 1
MAX_VALUE_NUMBER = 500


class AppUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    email = models.EmailField(
        error_messages={'unique': 'Email has been used from another user ,please enter a different email.'},
        unique=True,
        null=False,
        blank=False,
    )
    USERNAME_FIELD = 'email'
    is_staff = models.BooleanField(
        default=False,
        null=False,
        blank=False,
    )
    objects = AppUserManager()


class Profile(models.Model):
    first_name = models.CharField(max_length=MAX_LENGTH_FIRST_NAME, validators=[
        check_name_contains_only_letters,
        MinLengthValidator(MIN_LENGTH_FIRST_NAME),
    ])

    last_name = models.CharField(
        max_length=MAX_LENGTH_LAST_NAME,
        validators=[
            check_name_contains_only_letters,
            MinLengthValidator(MIN_LENGTH_LAST_NAME),
        ])

    city = models.CharField(
        max_length=MAX_LENGTH_CITY_NAME,
        validators=[
            MinLengthValidator(MIN_LENGTH_CITY_NAME),
        ])
    street = models.CharField(
        max_length=MAX_LENGTH_STREET_NAME,
        validators=[
            MinLengthValidator(MIN_LENGTH_STREET_NAME),
        ])
    number = models.PositiveIntegerField(
        validators=[
            MinValueValidator(MIN_VALUE_NUMBER),
        ])
    user = models.OneToOneField(AppUser, primary_key=True, on_delete=models.CASCADE)
    image = models.URLField(null=True, blank=True, )

    def __str__(self):
        return f"{str(self.pk)}"
