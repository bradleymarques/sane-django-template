from django.contrib.auth.views import (
    PasswordResetCompleteView as DjangoPasswordResetCompleteView,
)
from django.urls import reverse_lazy

from core import _
from core.forms import Notice


class PasswordResetCompleteView(DjangoPasswordResetCompleteView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        notice: Notice = Notice(
            title=_("Password reset complete"),
            texts=[
                _("Your password has been set. You may go ahead and log in now."),
            ],
            submit_button_url=reverse_lazy("users:login"),
            submit_button_text=_("Go to the login form"),
        )

        context.update({"notice": notice})
        return context
