from rest_framework import serializers

from .models import RecycleBin


class RecycleBinSerializer(
    serializers.ModelSerializer
):

    class Meta:

        model = RecycleBin

        fields = [
            "id",
            "file_name",
            "deleted_at"
        ]