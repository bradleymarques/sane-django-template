from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView
from rules.contrib.views import PermissionRequiredMixin

from users.models import User


class UserDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = User
    context_object_name = "detail_user"
    permission_required = "users.view_user"
