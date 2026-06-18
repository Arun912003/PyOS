from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import (
    IsAuthenticated
)

from .services import SearchService

from apps.history.services import (
    HistoryService
)

from apps.logs.services import (
    LogService
)


class SearchView(APIView):

    permission_classes = [
        IsAuthenticated
    ]

    def get(self, request):

        query = request.GET.get(
            "q",
            ""
        )

        results = SearchService.search(
            query,
            request.user
        )

        HistoryService.log_command(
            request.user,
            f"search {query}"
        )

        LogService.log_action(
            request.user,
            f"Searched for {query}"
        )

        return Response(
            results
        )