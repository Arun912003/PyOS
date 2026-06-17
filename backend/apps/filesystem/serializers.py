from rest_framework import serializers

from .models import Directory
from .models import File


class DirectorySerializer(
    serializers.ModelSerializer
):

    class Meta:

        model = Directory

        fields = [
            "id",
            "name",
            "parent",
            "created_at"
        ]

class FileSerializer(
    serializers.ModelSerializer
):

    class Meta:

        model = File

        fields = [
            "id",
            "name",
            "content",
            "directory",
            "permission"
        ]