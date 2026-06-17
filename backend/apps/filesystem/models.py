from django.db import models

from apps.users.models import User


class Directory(models.Model):

    name = models.CharField(
        max_length=255
    )

    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="directories",
        null=True,
        blank=True
    )

    parent = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        related_name="subdirectories",
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):

        return self.name


class File(models.Model):

    class PermissionChoices(
        models.TextChoices
    ):

        READ = "READ", "Read"

        WRITE = "WRITE", "Write"

        READ_WRITE = (
            "READ_WRITE",
            "Read Write"
        )

    name = models.CharField(
        max_length=255
    )

    content = models.TextField(
        blank=True
    )

    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="files",
        null=True,
        blank=True
    )

    directory = models.ForeignKey(
        Directory,
        on_delete=models.CASCADE,
        related_name="files"
    )

    permission = models.CharField(
        max_length=20,
        choices=PermissionChoices.choices,
        default=PermissionChoices.WRITE
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):

        return self.name