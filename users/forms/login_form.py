from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy

from core import _
from core.forms import BaseFormMixin, Button


class LoginForm(AuthenticationForm, BaseFormMixin):
    form_title = _("Login")
    form_submit_button_text = _("Login")
    form_tertiary_buttons = [
        Button(text=_("Forgot password?"), url=reverse_lazy("users:password-reset")),
        Button(text=_("Register"), url=reverse_lazy("users:register")),
    ]
