from http import HTTPStatus
from typing import Dict

from django.test import TestCase

from users.models import User


class BaseTest(TestCase):
    """
    Base class for all unit tests, containing useful, reusable functions.
    """

    def login(self, user: User, password: str = "password") -> bool:
        """
        Logs a user in by first setting their password to something known.
        """
        user.set_password(password)
        user.save()
        return self.client.login(username=user.username, password=password)

    def assert_unauthenticated_get(self, path: str):
        response = self.client.get(path, follow=True)
        login_url: str = f"/users/login/?next={path}"
        self.assertRedirects(response, login_url)

    def assert_unauthenticated_post(self, path: str, data: Dict):
        response = self.client.post(path, data=data, follow=True)
        login_url: str = f"/users/login/?next={path}"
        self.assertRedirects(response, login_url)

    def assert_unauthorized_get(self, path: str):
        response = self.client.get(path, follow=True)
        self.assertEqual(response.status_code, HTTPStatus.FORBIDDEN)
