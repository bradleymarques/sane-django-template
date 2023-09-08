from django.contrib.auth.views import (
    PasswordChangeDoneView as DjangoPasswordChangeDoneView,
)
from django.urls import reverse_lazy

from core import _
from core.forms.objects import Notice


class PasswordChangeDoneView(DjangoPasswordChangeDoneView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        notice: Notice = Notice(
            title=_("Password changed successfully"),
            texts=[
                _("Your password has been changed."),
                _(
                    "You will not be logged out now, but you will need to enter your new password on your next login."
                ),
            ],
            submit_button_url=reverse_lazy(
                "users:users-detail",
                kwargs={"pk": self.request.user.pk},
            ),
            submit_button_text=_("OK"),
        )

        context.update({"notice": notice})
        return context
