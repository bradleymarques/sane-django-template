from typing import List

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

from core import _
from core.forms import BaseFormMixin, Button
from users.models.user import User


class RegistrationForm(UserCreationForm, BaseFormMixin):
    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "password1",
            "password2",
        )

    form_title: str = _("Register")
    form_submit_button_text: str = _("Register")
    form_tertiary_buttons: List[Button] = [
        Button(text=_("Login"), url=reverse_lazy("users:login"))
    ]
