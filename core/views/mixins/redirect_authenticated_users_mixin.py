from django.contrib.auth.mixins import AccessMixin
from django.http import HttpResponseRedirect
from django.urls import reverse


class RedirectAuthenticatedUsersMixin(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse("rate-my-pet:pet-pictures-list"))

        return super().dispatch(request, *args, **kwargs)
