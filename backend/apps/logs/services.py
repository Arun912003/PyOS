from .models import Log


class LogService:

    @staticmethod
    def log_action(
        user,
        action
    ):

        Log.objects.create(
            user=user,
            action=action
        )