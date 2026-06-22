from .models import Directory
from .models import File


class DirectoryService:

    @staticmethod
    def create_directory(
        name,
        owner,
        parent=None
    ):

        directory = Directory.objects.create(
            name=name,
            owner=owner,
            parent=parent
        )

        return directory
    
    
    @staticmethod
    def list_directories(owner):

        return Directory.objects.filter(
            owner=owner,
            parent=owner.current_directory
        )

    @staticmethod
    def rename_directory(
        directory_id,
        new_name,
        owner
    ):

        directory = Directory.objects.get(
            id=directory_id,
            owner=owner
        )

        directory.name = new_name

        directory.save()

        return directory
    
    @staticmethod
    def delete_directory(
        directory_id,
        owner
    ):

        directory = Directory.objects.get(
            id=directory_id,
            owner=owner
        )

        directory.delete()


class FileService:

    @staticmethod
    def list_files(owner):

        return File.objects.filter(
            owner=owner,
            directory=owner.current_directory
        )

    @staticmethod
    def create_file(
        name,
        directory,
        owner
    ):

        file = File.objects.create(
            name=name,
            directory=directory,
            owner=owner
        )

        return file
    
    @staticmethod
    def get_file(
        file_id,
        owner
    ):

        return File.objects.get(
            id=file_id,
            owner=owner
        )
    
    @staticmethod
    def write_file(
        file_id,
        owner,
        content
    ):

        file = File.objects.get(
            id=file_id,
            owner=owner
        )

        file.content = content

        file.save()

        return file
    
    @staticmethod
    def delete_file(
        file_id,
        owner
    ):

        file = File.objects.get(
            id=file_id,
            owner=owner
        )

        file.delete()

    @staticmethod
    def rename_file(
        file_id,
        owner,
        new_name
    ):

        file = File.objects.get(
            id=file_id,
            owner=owner
        )

        file.name = new_name

        file.save()

        return file

    @staticmethod
    def change_permission(
        file_id,
        owner,
        permission
    ):

        file = File.objects.get(
            id=file_id,
            owner=owner
        )

        file.permission = permission

        file.save()

        return file
    
    @staticmethod
    def move_file(
        file_id,
        owner,
        directory
    ):

        file = File.objects.get(
            id=file_id,
            owner=owner
        )

        file.directory = directory

        file.save()

        return file
    
    @staticmethod
    def copy_file(
        file_id,
        owner,
        new_name
    ):

        file = File.objects.get(
            id=file_id,
            owner=owner
        )

        copied_file = File.objects.create(
            name=new_name,
            content=file.content,
            owner=file.owner,
            directory=file.directory,
            permission=file.permission
        )

        return copied_file
    
    @staticmethod
    def move_file(
        file_id,
        owner,
        directory
    ):

        file = File.objects.get(
            id=file_id,
            owner=owner
        )

        file.directory = directory

        file.save()

        return file
    
    @staticmethod
    def copy_file(
        file_id,
        owner,
        new_name
    ):

        file = File.objects.get(
            id=file_id,
            owner=owner
        )

        copied_file = File.objects.create(
            name=new_name,
            content=file.content,
            owner=file.owner,
            directory=file.directory,
            permission=file.permission
        )

        return copied_file
    
    @staticmethod
    def get_tree(owner):

        directories = Directory.objects.filter(
            owner=owner
        )

        files = File.objects.filter(
            owner=owner
        )

        return {
            "directories": directories,
            "files": files
        }