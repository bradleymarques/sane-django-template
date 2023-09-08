from django.contrib.auth.forms import PasswordResetForm as DjangoPasswordResetForm

from core import _
from core.forms import BaseFormMixin


class PasswordResetForm(DjangoPasswordResetForm, BaseFormMixin):
    title: str = _("Reset password")
    subtitle_help_text = _(
        "Forgotten your password? Enter your email address below and we'll send you instructions to reset it."
    )
    submit_button_text: str = _("Send password reset instructions")
