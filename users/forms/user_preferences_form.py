from core import _
from core.forms import BaseModelForm
from users.models.user_preferences import UserPreferences


class UserPreferencesForm(BaseModelForm):
    class Meta:
        model = UserPreferences
        fields = ["theme", "profile_picture"]

    form_title = _("Change your preferences")
    form_submit_button_text = _("Save")
    form_accepts_files = True
