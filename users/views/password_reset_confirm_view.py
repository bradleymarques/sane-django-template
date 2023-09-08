from django.contrib.auth.views import (
    PasswordResetConfirmView as DjangoPasswordResetConfirmView,
)
from django.urls import reverse_lazy

from users.forms import SetPasswordForm


class PasswordResetConfirmView(DjangoPasswordResetConfirmView):
    form_class = SetPasswordForm
    success_url = reverse_lazy("users:password-reset-complete")
