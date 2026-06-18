from django.urls import path

from .views import (
    RegisterView,
    ProfileView,
    ListUsersView,
    LogoutView,
    HelpView
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [

    path(
        "register/",
        RegisterView.as_view(),
        name="register"
    ),

    path(
        "login/",
        TokenObtainPairView.as_view(),
        name="login"
    ),

    path(
        "refresh/",
        TokenRefreshView.as_view(),
        name="refresh"
    ),

    path(
    "me/",
    ProfileView.as_view(),
    name="profile"
    ),

    path(
    "whoami/",
    ProfileView.as_view(),
    name="whoami"
    ),
    path(
    "list/",
    ListUsersView.as_view(),
    name="list-users"
    ),

    path(
    "logout/",
    LogoutView.as_view(),
    name="logout"
    ),

    path(
    "help/",
    HelpView.as_view(),
    name="help"
    ),
]