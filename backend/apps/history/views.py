from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import (
    IsAuthenticated
)

from .models import CommandHistory
from .serializers import (
    CommandHistorySerializer
)


class HistoryListView(APIView):

    permission_classes = [
        IsAuthenticated
    ]

    def get(self, request):

        history = (
            CommandHistory.objects.filter(
                user=request.user
            ).order_by("-created_at")
        )

        serializer = (
            CommandHistorySerializer(
                history,
                many=True
            )
        )

        return Response(
            serializer.data
        )