from http import HTTPStatus
from typing import Dict

from django.urls import reverse

from core.tests.base_test import BaseTest
from users.factories import UserFactory
from users.models import User, UserPreferences
from users.objects import Theme


class TestUserPreferencesUpdateView(BaseTest):
    def setUp(self) -> None:
        self.user: User = UserFactory.create()

        self.user_preferences: UserPreferences = self.user.user_preferences
        self.user_preferences.theme = Theme.LIGHT
        self.user_preferences.save()

        self.path = reverse(
            "users:user-preferences-update", kwargs={"pk": self.user_preferences.pk}
        )

    def test_an_unauthenticated_user_cannot_view_the_page(self):
        self.assert_unauthenticated_get(self.path)

    def test_a_user_cannot_view_another_users_preferences_page(self):
        another_user: User = UserFactory.create()
        self.login(another_user)
        self.assert_unauthorized_get(self.path)

    def test_a_user_can_view_their_own_preferences_page(self):
        self.login(self.user)
        response = self.client.get(self.path)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed("users/user_preferences_form.html")
        self.assertContains(response, "Change your preferences")
        self.assertContains(response, "Theme")
        self.assertContains(response, "Light")
        self.assertContains(response, "Dark")

    def test_a_user_cannot_update_another_users_preferences(self):
        another_user: User = UserFactory.create()
        self.login(another_user)
        form_data: Dict = {"theme": Theme.DARK.value}

        response = self.client.post(self.path, data=form_data)
        self.assertEqual(response.status_code, HTTPStatus.FORBIDDEN)

    def test_a_user_can_update_their_preferences(self):
        self.login(self.user)
        form_data: Dict = {"theme": Theme.DARK.value}

        response = self.client.post(self.path, data=form_data, follow=True)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(response, "Successfully updated preferences!")

        self.user_preferences.refresh_from_db()
        self.assertEqual(Theme(self.user_preferences.theme), Theme.DARK)
