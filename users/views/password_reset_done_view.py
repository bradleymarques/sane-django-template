from django.contrib.auth.views import (
    PasswordResetDoneView as DjangoPasswordResetDoneView,
)
from django.urls import reverse_lazy

from core import _
from core.forms.objects import Notice


class PasswordResetDoneView(DjangoPasswordResetDoneView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        notice: Notice = Notice(
            title=_("Password reset instructions sent"),
            texts=[
                _(
                    "We've emailed you instructions for setting your password, if an account exists with the email you entered. You should receive them shortly."
                ),
                _(
                    "If you don't receive an email, please make sure you've entered the address you registered with, and check your spam folder."
                ),
            ],
            submit_button_url=reverse_lazy("pages:home"),
            submit_button_text=_("Go back to the home page"),
        )

        context.update({"notice": notice})
        return context
