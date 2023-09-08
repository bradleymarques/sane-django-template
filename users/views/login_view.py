from django.contrib.auth.views import LoginView as DjangoDefaultLoginView

from core.views.mixins import RedirectAuthenticatedUsersMixin
from users.forms import LoginForm


class LoginView(RedirectAuthenticatedUsersMixin, DjangoDefaultLoginView):
    redirect_authenticated_user = True
    form_class = LoginForm
