from django.db import models

from apps.users.models import User


class CommandHistory(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="command_history"
    )

    command = models.CharField(
        max_length=255
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):

        return (
            f"{self.user.username}"
            f" - "
            f"{self.command}"
        )