from .models import RecycleBin

from apps.filesystem.models import (
    File
)


class RecycleBinService:

    @staticmethod
    def move_to_recycle_bin(
        file
    ):

        RecycleBin.objects.create(
            user=file.owner,
            file_name=file.name,
            content=file.content,
            directory=file.directory,
            permission=file.permission
        )

    @staticmethod
    def restore_file(
        recycle_file
    ):

        File.objects.create(
            name=recycle_file.file_name,
            content=recycle_file.content,
            owner=recycle_file.user,
            directory=recycle_file.directory,
            permission=recycle_file.permission
        )

        recycle_file.delete()