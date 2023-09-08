from django.contrib.auth.forms import SetPasswordForm as DjangoSetPasswordForm

from core import _
from core.forms import BaseFormMixin


class SetPasswordForm(DjangoSetPasswordForm, BaseFormMixin):
    form_title: str = _("Reset password")
    form_subtitle_help_text = _(
        "You're probably here because you wanted to reset your password. Please enter a new password below."
    )
    form_submit_button_text: str = _("Reset password")
