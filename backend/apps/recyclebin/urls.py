from django.urls import path

from .views import (
    RecycleBinListView,
    RestoreFileView,
    EmptyRecycleBinView
)

urlpatterns = [

    path(
        "",
        RecycleBinListView.as_view(),
        name="recycle-bin"
    ),

    path(
        "<int:recycle_id>/restore/",
        RestoreFileView.as_view(),
        name="restore-file"
    ),

    path(
        "empty/",
        EmptyRecycleBinView.as_view(),
        name="empty-recycle-bin"
    ),
]