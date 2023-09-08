from django.db.models import TextChoices

from core import _


class Theme(TextChoices):
    LIGHT = "light", _("Light")
    DARK = "dark", _("Dark")
    AUTO = "auto", _("Auto")


DEFAULT_THEME = Theme.AUTO
