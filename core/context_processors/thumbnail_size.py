from typing import Dict

from django.conf import settings


def thumbnail_size(_request) -> Dict:
    return {
        "THUMBNAIL_WIDTH": settings.IMAGES.get("THUMBNAIL_WIDTH"),
        "THUMBNAIL_HEIGHT": settings.IMAGES.get("THUMBNAIL_HEIGHT"),
    }
