from django.urls import path

from users.views import (
    LoginView,
    LogoutView,
    PasswordChangeDoneView,
    PasswordChangeView,
    PasswordResetCompleteView,
    PasswordResetConfirmView,
    PasswordResetDoneView,
    PasswordResetView,
    RegistrationView,
    UserDetailView,
    UserPreferencesUpdateView,
)

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("password_change/", PasswordChangeView.as_view(), name="password-change"),
    path(
        "password_change/done/",
        PasswordChangeDoneView.as_view(),
        name="password-change-done",
    ),
    path("password_reset/", PasswordResetView.as_view(), name="password-reset"),
    path(
        "password_reset/done/",
        PasswordResetDoneView.as_view(),
        name="password-reset-done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        PasswordResetConfirmView.as_view(),
        name="password-reset-confirm",
    ),
    path(
        "reset/done/",
        PasswordResetCompleteView.as_view(),
        name="password-reset-complete",
    ),
    path("users/new/", RegistrationView.as_view(), name="register"),
    path("users/<int:pk>/", UserDetailView.as_view(), name="users-detail"),
    path(
        "user_preferences/<int:pk>/",
        UserPreferencesUpdateView.as_view(),
        name="user-preferences-update",
    ),
]
