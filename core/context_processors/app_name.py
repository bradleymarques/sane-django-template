from typing import Dict

from django.conf import settings


def app_name(request) -> Dict:
    return {"APP_NAME": settings.APP_NAME}
