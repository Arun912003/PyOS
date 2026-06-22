from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .serializers import DirectorySerializer
from .services import DirectoryService
from .serializers import FileSerializer
from .services import FileService
from apps.history.services import HistoryService
from apps.logs.services import (
    LogService
)

from apps.recyclebin.services import (
    RecycleBinService
)
from .models import(
    Directory,
    File
) 

from apps.history.services import (
    HistoryService
)
from apps.filesystem.models import (
    File,
    Directory
)

from apps.recyclebin.models import (
    RecycleBin
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
                parent=request.user.current_directory
            )
            HistoryService.log_command(
                    request.user,
                    f"mkdir {directory.name}"
                )
            
            LogService.log_action(
                request.user,
                f"Created directory {directory.name}"
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

        HistoryService.log_command(
            request.user,
            "ls"
        )

        LogService.log_action(
            request.user,
            "Listed directories"
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
        

        directory = Directory.objects.get(
            id=directory_id,
            owner=request.user
        )

        old_name = directory.name

        directory = (
            DirectoryService.rename_directory(
                directory_id=directory_id,
                new_name=request.data["name"],
                owner=request.user
            )
        )

        HistoryService.log_command(
            request.user,
            f"rename {old_name} -> {directory.name}"
        )

        LogService.log_action(
            request.user,
            f"Renamed directory {old_name} to {directory.name}"
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

        directory = Directory.objects.get(
            id=directory_id,
            owner=request.user
        )

        directory_name = directory.name

        DirectoryService.delete_directory(
            directory_id=directory_id,
            owner=request.user
        )

        HistoryService.log_command(
            request.user,
            f"rmdir {directory_name}"
        )

        LogService.log_action(
            request.user,
            f"Deleted directory {directory_name}"
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
            data=request.data,
            partial =True
        )

        if serializer.is_valid():

            file = FileService.create_file(
                name=serializer.validated_data["name"],
                directory=request.user.current_directory,
                owner=request.user
            )

            HistoryService.log_command(
                request.user,
                f"create {file.name}"
            )

            LogService.log_action(
                request.user,
                f"Created file {file.name}"
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

        HistoryService.log_command(
            request.user,
            f"read {file.name}"
        )

        LogService.log_action(
            request.user,
            f"Read file {file.name}"
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

        HistoryService.log_command(
            request.user,
            f"write {file.name}"
        )

        LogService.log_action(
            request.user,
            f"Updated file {file.name}"
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

        file = FileService.get_file(
            file_id=file_id,
            owner=request.user
        )

        file_name = file.name

        RecycleBinService.move_to_recycle_bin(
            file
        )

        FileService.delete_file(
            file_id=file_id,
            owner=request.user
        )

        HistoryService.log_command(
            request.user,
            f"delete {file_name}"
        )

        LogService.log_action(
            request.user,
            f"Deleted file {file_name}"
        )

        return Response(
            {
                "message":
                "File deleted successfully"
            }
        )
    
class FileRenameView(APIView):

    permission_classes = [
        IsAuthenticated
    ]

    def patch(
        self,
        request,
        file_id
    ):

        file = File.objects.get(
            id=file_id,
            owner=request.user
        )

        old_name = file.name

        file = FileService.rename_file(
            file_id=file_id,
            owner=request.user,
            new_name=request.data["name"]
        )

        HistoryService.log_command(
            request.user,
            f"rename {old_name} -> {file.name}"
        )

        LogService.log_action(
            request.user,
            f"Renamed file {old_name} to {file.name}"
        )

        return Response(
            {
                "message":
                "File renamed successfully"
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

        HistoryService.log_command(
            request.user,
            f"chmod {file.name}"
        )

        LogService.log_action(
            request.user,
            f"Changed permission of {file.name}"
        )

        return Response(
            {
                "message":
                "Permission updated successfully"
            }
        )
    
class FileListView(APIView):

    permission_classes = [
        IsAuthenticated
    ]

    def get(self, request):

        files = FileService.list_files(
            request.user
        )

        serializer = FileSerializer(
            files,
            many=True
        )

        return Response(
            serializer.data
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
        HistoryService.log_command(
            request.user,
            f"fileinfo {file.name}"
        )

        LogService.log_action(
            request.user,
            f"Viewed file info for {file.name}"
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

        file = FileService.move_file(
            file_id=file_id,
            owner=request.user,
            directory=directory
        )
        HistoryService.log_command(
            request.user,
            f"move {file.name}"
        )

        LogService.log_action(
            request.user,
            f"Moved file {file.name}"
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

        HistoryService.log_command(
            request.user,
            f"copy {file.name}"
        )

        LogService.log_action(
            request.user,
            f"Copied file {file.name}"
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

        HistoryService.log_command(
            request.user,
            "tree"
        )

        LogService.log_action(
            request.user,
            "Viewed filesystem tree"
        )

        return Response(
            {
                "directories":
                [d.name for d in directories],

                "files":
                [f.name for f in files]
            }
        )
    
class DiskInfoView(APIView):

    permission_classes = [
        IsAuthenticated
    ]

    def get(self, request):

        HistoryService.log_command(
            request.user,
            "diskinfo"
        )

        LogService.log_action(
            request.user,
            "Viewed disk information"
        )

        return Response(
            {
                "directories":
                    Directory.objects.filter(
                        owner=request.user
                    ).count(),

                "files":
                    File.objects.filter(
                        owner=request.user
                    ).count(),

                "recycle_bin":
                    RecycleBin.objects.filter(
                        user=request.user
                    ).count()
            }
        )
    
class PwdView(APIView):

    permission_classes = [
        IsAuthenticated
    ]

    def get(self, request):

        directory = (
            request.user.current_directory
        )

        if not directory:

            path = "root"

        else:

            parts = []

            current = directory

            while current:

                parts.append(
                    current.name
                )

                current = current.parent

            parts.reverse()

            path = (
                "root/" +
                "/".join(parts)
            )

        HistoryService.log_command(
            request.user,
            "pwd"
        )

        LogService.log_action(
            request.user,
            f"Viewed path {path}"
        )

        return Response(
            {
                "path": path
            }
        )
    
class CdView(APIView):

    permission_classes = [
        IsAuthenticated
    ]

    def post(self, request):

        target = request.data.get(
            "directory"
        )

        current = (
            request.user.current_directory
        )

        if target == "..":

            if current:

                request.user.current_directory = (
                    current.parent
                )

                request.user.save()

            HistoryService.log_command(
                request.user,
                "cd .."
            )

            LogService.log_action(
                request.user,
                "Changed directory"
            )

            return Response(
                {
                    "message":
                    "Directory changed"
                }
            )

        directory = (
            Directory.objects.filter(
                owner=request.user,
                name=target,
                parent=current
            ).first()
        )

        if not directory:

            return Response(
                {
                    "error":
                    "Directory not found"
                },
                status=404
            )

        request.user.current_directory = (
            directory
        )

        request.user.save()

        HistoryService.log_command(
            request.user,
            f"cd {target}"
        )

        LogService.log_action(
            request.user,
            f"Changed directory to {target}"
        )

        return Response(
            {
                "message":
                "Directory changed"
            }
        )