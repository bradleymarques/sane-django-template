from typing import Dict, Optional

from users.models import User
from users.objects.theme import DEFAULT_THEME


def bootstrap_theme(request) -> Dict:
    user: Optional[User] = request.user

    if user and user.is_authenticated:
        return {"BOOTSTRAP_THEME": user.user_preferences.theme}
    return {"BOOTSTRAP_THEME": DEFAULT_THEME}
