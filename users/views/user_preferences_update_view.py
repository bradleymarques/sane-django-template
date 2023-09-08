from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import UpdateView
from rules.contrib.views import PermissionRequiredMixin

from core import _
from users.forms.user_preferences_form import UserPreferencesForm
from users.models.user_preferences import UserPreferences


class UserPreferencesUpdateView(
    LoginRequiredMixin,
    PermissionRequiredMixin,
    UpdateView,
):
    model = UserPreferences
    form_class = UserPreferencesForm
    permission_required = "users.update_userpreferences"
    template_name = "users/user_preferences_form.html"

    def get_success_url(self) -> str:
        messages.success(self.request, _("Successfully updated preferences!"))
        return reverse(
            "users:user-preferences-update",
            kwargs={"pk": self.get_object().pk},
        )
