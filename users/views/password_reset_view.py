from django.contrib.auth.views import PasswordResetView as DjangoPasswordResetView
from django.urls import reverse_lazy

from users.forms import PasswordResetForm


class PasswordResetView(DjangoPasswordResetView):
    form_class = PasswordResetForm
    success_url = reverse_lazy("users:password-reset-done")
    email_template_name = "registration/password_reset_email.html"
