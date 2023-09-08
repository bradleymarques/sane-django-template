from django.db import models
from rules.contrib.models import RulesModel


class BaseModel(RulesModel):
    class Meta:
        abstract = True
        default_permissions = ()
        rules_permissions = {}

    created_at = models.DateTimeField(auto_now_add=True, null=False)
    updated_at = models.DateTimeField(auto_now=True, null=False)
