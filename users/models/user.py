import rules
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from rules.contrib.models import RulesModel


@rules.predicate
def is_self(current_user, user_model):
    return current_user == user_model


class User(AbstractUser, RulesModel):
    class Meta:
        default_permissions = ()
        rules_permissions = {
            "create": rules.always_allow,
            "view": rules.is_superuser | is_self,  # type: ignore
            "update": rules.is_superuser | is_self,  # type: ignore
            "delete": rules.is_superuser,
        }

    email = models.EmailField(
        _("email"),
        blank=False,
        null=False,
        unique=True,
        error_messages={
            "unique": _("A user with that email already exists."),
        },
    )

    def __str__(self) -> str:
        return f"@{self.username}"
