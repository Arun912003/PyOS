from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    ROLE_CHOICES = (
        ("ADMIN", "Admin"),
        ("USER", "User"),
    )

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default="USER"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.username