from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .serializers import DirectorySerializer
from .services import DirectoryService
from .serializers import FileSerializer
from .services import FileService
from .models import(
    Directory,
    File
) 


class DirectoryCreateView(APIView):

    permission_classes = [
        IsAuthenticated
    ]

    def post(self, request):

        serializer = DirectorySerializer(
            data=request.data
        )

        if serializer.is_valid():

            directory = DirectoryService.create_directory(
                name=serializer.validated_data["name"],
                owner=request.user,
                parent=serializer.validated_data.get(
                    "parent"
                )
            )

            return Response(
                {
                    "id": directory.id,
                    "name": directory.name,
                    "message": "Directory created successfully"
                },
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
    
class DirectoryListView(APIView):

    permission_classes = [
        IsAuthenticated
    ]

    def get(self, request):

        directories = (
            DirectoryService.list_directories(
                request.user
            )
        )

        serializer = DirectorySerializer(
            directories,
            many=True
        )

        return Response(
            serializer.data
        )
    
class DirectoryRenameView(APIView):

    permission_classes = [
        IsAuthenticated
    ]

    def patch(
        self,
        request,
        directory_id
    ):

        directory = (
            DirectoryService.rename_directory(
                directory_id=directory_id,
                new_name=request.data["name"],
                owner=request.user
            )
        )

        return Response(
            {
                "message":
                "Directory renamed successfully"
            }
        )
    
class DirectoryDeleteView(APIView):

    permission_classes = [
        IsAuthenticated
    ]

    def delete(
        self,
        request,
        directory_id
    ):

        DirectoryService.delete_directory(
            directory_id=directory_id,
            owner=request.user
        )

        return Response(
            {
                "message":
                "Directory deleted successfully"
            }
        )
    
class FileCreateView(APIView):

    permission_classes = [
        IsAuthenticated
    ]

    def post(self, request):

        serializer = FileSerializer(
            data=request.data
        )

        if serializer.is_valid():

            file = FileService.create_file(
                name=serializer.validated_data["name"],
                directory=serializer.validated_data["directory"],
                owner=request.user
            )

            return Response(
                {
                    "id": file.id,
                    "name": file.name,
                    "message": "File created successfully"
                }
            )

        return Response(
            serializer.errors,
            status=400
        )
    
class FileReadView(APIView):

    permission_classes = [
        IsAuthenticated
    ]

    def get(
        self,
        request,
        file_id
    ):

        file = FileService.get_file(
            file_id=file_id,
            owner=request.user
        )

        serializer = FileSerializer(
            file
        )

        return Response(
            serializer.data
        )
    
class FileWriteView(APIView):

    permission_classes = [
        IsAuthenticated
    ]

    def patch(
        self,
        request,
        file_id
    ):

        file = FileService.write_file(
            file_id=file_id,
            owner=request.user,
            content=request.data["content"]
        )

        return Response(
            {
                "message":
                "File updated successfully"
            }
        )
    
class FileDeleteView(APIView):

    permission_classes = [
        IsAuthenticated
    ]

    def delete(
        self,
        request,
        file_id
    ):

        FileService.delete_file(
            file_id=file_id,
            owner=request.user
        )

        return Response(
            {
                "message":
                "File deleted successfully"
            }
        )
    
class FilePermissionView(APIView):

    permission_classes = [
        IsAuthenticated
    ]

    def patch(
        self,
        request,
        file_id
    ):

        FileService.change_permission(
            file_id=file_id,
            owner=request.user,
            permission=request.data["permission"]
        )

        return Response(
            {
                "message":
                "Permission updated successfully"
            }
        )
    
class FileInfoView(APIView):

    permission_classes = [
        IsAuthenticated
    ]

    def get(
        self,
        request,
        file_id
    ):

        file = FileService.get_file(
            file_id=file_id,
            owner=request.user
        )

        return Response(
            {
                "id": file.id,
                "name": file.name,
                "owner": file.owner.username,
                "permission": file.permission,
                "created_at": file.created_at,
                "updated_at": file.updated_at
            }
        )
    
class FileMoveView(APIView):

    permission_classes = [
        IsAuthenticated
    ]

    def patch(
        self,
        request,
        file_id
    ):

        directory = Directory.objects.get(
            id=request.data["directory"]
        )

        FileService.move_file(
            file_id=file_id,
            owner=request.user,
            directory=directory
        )

        return Response(
            {
                "message":
                "File moved successfully"
            }
        )
    
class FileCopyView(APIView):

    permission_classes = [
        IsAuthenticated
    ]

    def post(
        self,
        request,
        file_id
    ):

        file = FileService.copy_file(
            file_id=file_id,
            owner=request.user,
            new_name=request.data["name"]
        )

        return Response(
            {
                "id": file.id,
                "name": file.name,
                "message": "File copied successfully"
            }
        )
    
class TreeView(APIView):

    permission_classes = [
        IsAuthenticated
    ]

    def get(self, request):

        directories = Directory.objects.filter(
            owner=request.user
        )

        files = File.objects.filter(
            owner=request.user
        )

        return Response(
            {
                "directories":
                [d.name for d in directories],

                "files":
                [f.name for f in files]
            }
        )