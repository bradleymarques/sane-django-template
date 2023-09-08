from typing import Any

from django.urls import reverse
from django.views.generic.base import RedirectView


class HomePageRedirectView(RedirectView):
    def get_redirect_url(self, *args: Any, **kwargs: Any) -> str | None:
        if self.request.user and self.request.user.is_authenticated:
            return reverse("rate-my-pet:pet-pictures-list")
        else:
            return reverse("pages:home")
