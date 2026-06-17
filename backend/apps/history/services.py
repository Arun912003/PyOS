from .models import CommandHistory


class HistoryService:

    @staticmethod
    def log_command(
        user,
        command
    ):

        CommandHistory.objects.create(
            user=user,
            command=command
        )