from django.views.generic import TemplateView

from core.views.mixins import RedirectAuthenticatedUsersMixin


class HomeView(RedirectAuthenticatedUsersMixin, TemplateView):
    template_name = "pages/home.html"
