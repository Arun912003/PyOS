from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import (
    IsAuthenticated
)

from .models import RecycleBin
from .serializers import (
    RecycleBinSerializer
)
from .services import (
    RecycleBinService
)

from apps.history.services import (
    HistoryService
)

from apps.logs.services import (
    LogService
)

class RecycleBinListView(APIView):

    permission_classes = [
        IsAuthenticated
    ]

    def get(self, request):

        files = (
            RecycleBin.objects.filter(
                user=request.user
            ).order_by("-deleted_at")
        )

        serializer = (
            RecycleBinSerializer(
                files,
                many=True
            )
        )

        return Response(
            serializer.data
        )
    
class RestoreFileView(APIView):

    permission_classes = [
        IsAuthenticated
    ]

    def post(
        self,
        request,
        recycle_id
    ):

        recycle_file = (
            RecycleBin.objects.get(
                id=recycle_id,
                user=request.user
            )
        )

        file_name = (
            recycle_file.file_name
        )

        RecycleBinService.restore_file(
            recycle_file
        )

        HistoryService.log_command(
            request.user,
            f"restore {file_name}"
        )

        LogService.log_action(
            request.user,
            f"Restored file {file_name}"
        )

        return Response(
            {
                "message":
                "File restored successfully"
            }
        )
    
class EmptyRecycleBinView(APIView):

    permission_classes = [
        IsAuthenticated
    ]

    def delete(
        self,
        request
    ):

        RecycleBin.objects.filter(
            user=request.user
        ).delete()

        HistoryService.log_command(
            request.user,
            "empty recyclebin"
        )

        LogService.log_action(
            request.user,
            "Emptied recycle bin"
        )

        return Response(
            {
                "message":
                "Recycle bin emptied"
            }
        )