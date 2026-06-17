from django.db import models

from apps.users.models import User
from apps.filesystem.models import Directory


class RecycleBin(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="recycle_bin"
    )

    file_name = models.CharField(
        max_length=255
    )

    content = models.TextField(
        blank=True
    )

    directory = models.ForeignKey(
    Directory,
    on_delete=models.SET_NULL,
    null=True,
    blank=True
    )

    permission = models.CharField(
        max_length=20,
        default="WRITE"
    )

    deleted_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):

        return self.file_name