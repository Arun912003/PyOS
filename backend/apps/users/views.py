from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import RegisterSerializer
from .services import UserService
from rest_framework.permissions import IsAuthenticated
from .models import User
from .serializers import UserSerializer

from apps.history.services import (
    HistoryService
)

from apps.logs.services import (
    LogService
)

class RegisterView(APIView):

    def post(self, request):

        serializer = RegisterSerializer(
            data=request.data
        )

        if serializer.is_valid():

            UserService.create_user(
                serializer.validated_data
            )

            return Response(
                {
                    "message": "User registered successfully"
                },
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
    
class ProfileView(APIView):

    permission_classes = [
        IsAuthenticated
    ]

    def get(self, request):

        serializer = UserSerializer(
            request.user
        )

        return Response(
            serializer.data
        )
    
class ListUsersView(APIView):

    permission_classes = [
        IsAuthenticated
    ]

    def get(self, request):

        users = User.objects.all()

        serializer = UserSerializer(
            users,
            many=True
        )

        return Response(
            serializer.data
        )
    
class LogoutView(APIView):

    permission_classes = [
        IsAuthenticated
    ]

    def post(self, request):

        return Response(
            {
                "message":
                "Logged out successfully"
            }
        )
    
class HelpView(APIView):

    permission_classes = [
        IsAuthenticated
    ]

    def get(self, request):

        HistoryService.log_command(
            request.user,
            "help"
        )

        LogService.log_action(
            request.user,
            "Viewed help"
        )

        return Response(
            {
                "commands": [

                    "mkdir",
                    "ls",
                    "rename",
                    "rmdir",

                    "create",
                    "read",
                    "write",
                    "delete",

                    "chmod",
                    "move",
                    "copy",
                    "tree",
                    "fileinfo",

                    "search",

                    "history",
                    "logs",

                    "recyclebin",

                    "whoami",
                    "listusers",
                    "logout",

                    "diskinfo"
                ]
            }
        )