from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import CreateView
from verify_email.email_handler import send_verification_email

from core.views.mixins import RedirectAuthenticatedUsersMixin
from users.forms import RegistrationForm
from users.models import User, UserPreferences


class RegistrationView(RedirectAuthenticatedUsersMixin, CreateView):
    form_class = RegistrationForm
    template_name = "registration/register.html"

    def form_valid(self, form):
        inactive_user: User = send_verification_email(self.request, form)
        UserPreferences.objects.create(user=inactive_user)

        messages.success(
            self.request,
            f"Please check your email ({inactive_user.email}) for a link to activate your account.",
        )
        return HttpResponseRedirect(reverse("pages:home"))
