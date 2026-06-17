from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import (
    IsAuthenticated
)

from .models import Log
from .serializers import (
    LogSerializer
)


class LogListView(APIView):

    permission_classes = [
        IsAuthenticated
    ]

    def get(self, request):

        logs = (
            Log.objects.filter(
                user=request.user
            ).order_by("-created_at")
        )

        serializer = LogSerializer(
            logs,
            many=True
        )

        return Response(
            serializer.data
        )