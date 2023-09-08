from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.models import User, UserPreferences

admin.site.register(User, UserAdmin)
admin.site.register(UserPreferences)
