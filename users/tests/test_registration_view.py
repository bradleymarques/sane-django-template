from http import HTTPStatus
from typing import Dict

from django.urls import reverse

from core.tests import BaseTest
from users.factories import UserFactory
from users.models import User


class TestRegistrationView(BaseTest):
    def setUp(self) -> None:
        self.path: str = reverse("users:register")

    def test_an_authenticated_user_is_redirected(self):
        user: User = UserFactory.create()
        self.login(user)
        expected_url = reverse("rate-my-pet:pet-pictures-list")
        response = self.client.get(self.path, follow=True)
        self.assertRedirects(response, expected_url)

    def test_an_unauthenticated_user_can_view_the_page(self):
        response = self.client.get(self.path)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(response, "Username")
        self.assertContains(response, "Email")
        self.assertContains(response, "Password")
        self.assertContains(response, "Password confirmation")

    def test_an_unauthenticated_user_can_complete_the_form_and_an_inactive_user_is_created(
        self,
    ):
        email: str = "bobby.smith@example.com"

        form_data: Dict = {
            "username": "bobby_smith",
            "email": email,
            "password1": "S3Cr3t_P@55w0rD",
            "password2": "S3Cr3t_P@55w0rD",
        }

        response = self.client.post(self.path, data=form_data, follow=True)

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(
            response,
            f"Please check your email ({email}) for a link to activate your account.",
        )
        self.assertTemplateUsed("home.html")

        user: User = User.objects.last()
        self.assertIsNotNone(user)
        self.assertEqual("bobby_smith", user.username)
        self.assertFalse(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

        self.assertIsNotNone(user.user_preferences)

    def test_username_and_email_must_be_unique(self):
        username: str = "bobby"
        email: str = "bobby.smith@example.com"

        UserFactory.create(username=username, email=email)

        form_data: Dict = {
            "username": username,
            "email": email,
            "password1": "S3Cr3t_P@55w0rD",
            "password2": "S3Cr3t_P@55w0rD",
        }

        response = self.client.post(self.path, data=form_data)

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(response, "A user with that username already exists.")
        self.assertContains(response, "A user with that email already exists.")
