from typing import List

from django.core.exceptions import ImproperlyConfigured

from core.forms.objects import Button


class BaseFormMixin:
    form_title: str = "[FORM TITLE]"
    form_subtitle_help_text = None
    form_submit_button_text: str = "[SUBMIT BUTTON TEXT]"
    form_tertiary_buttons: List[Button] = []
    form_accepts_files: bool = False

    def enctype(self) -> str:
        if self.form_accepts_files:
            return "multipart/form-data"
        else:
            return "application/x-www-form-urlencoded"
