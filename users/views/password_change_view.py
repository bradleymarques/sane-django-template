from django.contrib.auth.views import PasswordChangeView as DjangoPasswordChangeView
from django.urls import reverse_lazy

from users.forms import PasswordChangeForm


class PasswordChangeView(DjangoPasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy("users:password-change-done")
