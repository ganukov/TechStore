from django.core.validators import MinValueValidator
from django.db import models

CHOICES = (('Laptop', 'Laptop'),
           ('Phone', 'Phone'),
           ('Console', 'Console'),
           )


class Product(models.Model):
    choice = models.CharField(
        max_length=25,
        choices=CHOICES,

    )
    name = models.CharField(
        max_length=50,
        null=True,
    )
    make = models.CharField(
        max_length=50,
    )
    price = models.FloatField(
        max_length=25,
        validators=[MinValueValidator(0), ],
    )
    image = models.URLField(

    )
    cpu = models.CharField(
        max_length=25,
        null=True,
        blank=True,
    )
    gpu = models.CharField(
        max_length=25,
        null=True,
        blank=True,
    )
    weight = models.FloatField(
        null=False,
        blank=False,
    )
    os = models.CharField(
        max_length=25,
        null=True,
        blank=True,
    )

    description = models.CharField(
        max_length=500,
        null=False,
        blank=False,

    )

    def __str__(self):
        return f"{self.name} {self.make}"
