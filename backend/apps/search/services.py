from django.db.models import Q

from apps.filesystem.models import (
    File,
    Directory
)


class SearchService:

    @staticmethod
    def search(
        query,
        user
    ):

        files = File.objects.filter(
            owner =user
        ).filter(
            Q(name__icontains=query) |
            Q(content__icontains=query) |
            Q(directory__name__icontains=query)

        )

        matched_directories = Directory.objects.filter(
            owner=user,
            name__icontains=query
        )

        file_directories = Directory.objects.filter(
            id__in=files.values_list(
            "directory_id",
            flat=True
            )
        )

        directories = (
            matched_directories |
            file_directories
        ).distinct()

        return {
            "files": [
                {
                    "id": file.id,
                    "name": file.name,
                    "directory": (
                        file.directory.name
                        if file.directory
                        else "root"
                    )
                }
                for file in files
            ],
            "directories": [
                {
                    "id": directory.id,
                    "name": directory.name
                }
                for directory in directories
            ]
        }