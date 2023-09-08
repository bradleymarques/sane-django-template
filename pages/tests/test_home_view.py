from http import HTTPStatus

from django.conf import settings
from django.urls import reverse

from core.tests import BaseTest
from users.factories import UserFactory
from users.models import User


class TestHomeView(BaseTest):
    def test_an_unauthenticated_user_can_view_the_home_page(self):
        response = self.client.get(reverse("pages:home"))

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(response, settings.APP_NAME)
        self.assertContains(response, "Login")
        self.assertContains(response, "Register")

    def test_an_authenticated_user_is_redirected_from_the_home_page(self):
        user: User = UserFactory.create()
        self.login(user)

        expected_url = reverse("rate-my-pet:pet-pictures-list")
        response = self.client.get(reverse("pages:home"), follow=True)
        self.assertRedirects(response, expected_url, HTTPStatus.FOUND, HTTPStatus.OK)
