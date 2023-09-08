from django.contrib.auth.forms import PasswordChangeForm as DjangoPasswordChangeForm

from core import _
from core.forms import BaseFormMixin


class PasswordChangeForm(DjangoPasswordChangeForm, BaseFormMixin):
    form_title: str = _("Change password")
    form_submit_button_text: str = _("Change password")
