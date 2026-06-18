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
            Q(content__icontains=query)
        )

        directories = Directory.objects.filter(
            owner=user,
            name__icontains=query
        )

        return {
            "files": [
                {
                    "id": file.id,
                    "name": file.name
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