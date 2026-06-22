from django.urls import path

from .views import (
    DirectoryCreateView,
    DirectoryListView,
    DirectoryRenameView,
    DirectoryDeleteView,
    FileCreateView,
    FileReadView,
    FileWriteView,
    FileDeleteView,
    FilePermissionView,
    FileInfoView,
    FileMoveView,
    FileCopyView,
    TreeView,
    DiskInfoView,
    PwdView,
    CdView,
    FileListView,
    FileRenameView
)

urlpatterns = [

    path(
        "directories/",
        DirectoryCreateView.as_view(),
        name="create-directory"
    ),
    path(
    "directories/list/",
    DirectoryListView.as_view(),
    name="list-directories"
    ),

    path(
    "directories/<int:directory_id>/rename/",
    DirectoryRenameView.as_view(),
    name="rename-directory"
    ),

    path(
    "directories/<int:directory_id>/",
    DirectoryDeleteView.as_view(),
    name="delete-directory"
    ),

    path(
    "files/",
    FileCreateView.as_view(),
    name="create-file"
    ),
    path(
    "files/<int:file_id>/",
    FileReadView.as_view(),
    name="read-file"
    ),

    path(
    "files/<int:file_id>/write/",
    FileWriteView.as_view(),
    name="write-file"
    ),
    path(
    "files/<int:file_id>/delete/",
    FileDeleteView.as_view(),
    name="delete-file"
    ),

    path(
    "files/<int:file_id>/rename/",
    FileRenameView.as_view()
),

    path(
    "files/<int:file_id>/permission/",
    FilePermissionView.as_view(),
    name="change-permission"
    ),

    path(
    "files/list/",
    FileListView.as_view(),
    name="list-files"
),

    path(
    "files/<int:file_id>/info/",
    FileInfoView.as_view(),
    name="file-info"
    ),
    path(
    "files/<int:file_id>/move/",
    FileMoveView.as_view(),
    name="move-file"
    ),

    path(
    "files/<int:file_id>/copy/",
    FileCopyView.as_view(),
    name="copy-file"
    ),

    path(
    "tree/",
    TreeView.as_view(),
    name="tree"
    ),
    path(
    "diskinfo/",
    DiskInfoView.as_view(),
    name="diskinfo"
    ),

    path(
    "pwd/",
    PwdView.as_view(),
    name="pwd"
    ),

    path(
    "cd/",
    CdView.as_view(),
    name="cd"
    ),
]