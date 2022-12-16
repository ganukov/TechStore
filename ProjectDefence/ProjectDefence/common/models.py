from ProjectDefence.accounts.models import Profile
from ProjectDefence.products.models import Product
from django.db import models


class Complaint(models.Model):
    first_name = models.CharField(
        max_length=10,
    )
    email = models.EmailField(
        max_length=25,
    )
    subject = models.CharField(
        max_length=15,
    )
    message = models.TextField(
        max_length=500,
    )

    def __str__(self):
        return f"{self.email} -- {self.subject}"
