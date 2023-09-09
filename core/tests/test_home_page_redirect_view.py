from django.urls import reverse

from core.tests import BaseTest
from users.factories import UserFactory
from users.models import User


class TestHomePageRedirectView(BaseTest):
    def test_an_unauthenticated_user_is_redirected_to_the_home_page(self):
        response = self.client.get("/")

        self.assertRedirects(response, reverse("pages:home"))
        self.assertTemplateUsed("home.html")

    def test_an_authenticated_user_is_redirected_to_their_own_page(self):
        user: User = UserFactory.create()
        self.login(user)

        response = self.client.get("/")

        self.assertRedirects(
            response,
            reverse(
                "users:user-preferences-update",
                kwargs={"pk": user.pk},
            ),
        )
        self.assertTemplateUsed("user_detail.html")
