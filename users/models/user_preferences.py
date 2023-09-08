from __future__ import annotations

import os
import re
import uuid
from typing import Any

import rules
from django.conf import settings
from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import SmartResize

from core.models import BaseModel
from users.models.user import User
from users.objects import Theme
from users.objects.theme import DEFAULT_THEME

FALLBACK_PROFILE_PICTURE_URL: str = os.path.join(
    settings.STATIC_URL,
    "users",
    "images",
    "placeholder_profile.png",
)


def profile_picture_file_path(instance: UserPreferences, filename: str) -> Any:
    file_extension: str = filename.split(".")[-1]
    unique_id: str = re.sub("-", "_", str(uuid.uuid4()))
    return f"users/{instance.user.pk}/profile_pictures/{unique_id}.{file_extension}"


@rules.predicate
def is_owner(user: User, user_preferences: UserPreferences):
    return user == user_preferences.user


class UserPreferences(BaseModel):
    class Meta:
        default_permissions = ()
        rules_permissions = {
            "create": rules.always_deny,
            "view": is_owner,
            "update": is_owner,
            "delete": rules.is_superuser,
        }
        indexes = [models.Index(fields=["user_id"])]

    user = models.OneToOneField(
        User,
        on_delete=models.RESTRICT,
        related_name="user_preferences",
    )
    theme = models.CharField(
        max_length=32,
        choices=Theme.choices,
        default=DEFAULT_THEME,
    )
    profile_picture: models.ImageField = models.ImageField(
        upload_to=profile_picture_file_path,
        null=True,
        blank=True,
    )
    profile_picture_thumbnail: ImageSpecField = ImageSpecField(
        source="profile_picture",
        processors=[
            SmartResize(
                width=settings.IMAGES.get("THUMBNAIL_WIDTH"),
                height=settings.IMAGES.get("THUMBNAIL_HEIGHT"),
            )
        ],
        format="JPEG",
        options={
            "quality": settings.IMAGES.get("THUMBNAIL_JPEG_QUALITY"),
        },
    )

    def __str__(self) -> str:
        return f"{self.user.__str__()}'s UserPreferences"

    def profile_picture_thumbnail_url_with_fallback(self) -> str:
        if bool(self.profile_picture_thumbnail):
            return self.profile_picture_thumbnail.url
        else:
            return FALLBACK_PROFILE_PICTURE_URL
