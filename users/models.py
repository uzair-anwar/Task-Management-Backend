from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('manager', 'Manager'),
        ('regular', 'Regular User'),
    )

    role = models.CharField(choices=ROLE_CHOICES,
                            max_length=10, default='regular')
