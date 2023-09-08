from django.urls import reverse

from core.tests import BaseTest
from users.factories import UserFactory
from users.models import User, UserPreferences
from users.objects.theme import DEFAULT_THEME, Theme


class TestTheming(BaseTest):
    def test_there_is_a_default_theme_for_the_login_and_register_and_home_pages(self):
        response_home = self.client.get(reverse("pages:home"))
        response_login = self.client.get(reverse("users:login"))
        response_register = self.client.get(reverse("users:register"))

        expected_html = f"data-bs-theme={DEFAULT_THEME.value}"

        self.assertContains(response_home, expected_html)
        self.assertContains(response_login, expected_html)
        self.assertContains(response_register, expected_html)

    def test_an_authenticated_user_sees_pages_in_the_theme_they_set(self):
        user: User = UserFactory.create()

        user_preferences: UserPreferences = user.user_preferences
        user_preferences.theme = Theme.LIGHT
        user_preferences.save()

        self.login(user)

        response_1 = self.client.get(
            reverse("users:users-detail", kwargs={"pk": user.pk})
        )

        self.assertContains(response_1, "data-bs-theme=light")

        user_preferences.theme = Theme.DARK
        user_preferences.save()

        response_2 = self.client.get(
            reverse("users:users-detail", kwargs={"pk": user.pk})
        )

        self.assertContains(response_2, "data-bs-theme=dark")
