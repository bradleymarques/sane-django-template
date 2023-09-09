from http import HTTPStatus

from django.urls import reverse

from core.tests import BaseTest
from users.factories import UserFactory
from users.models import User


class TestLoginView(BaseTest):
    def setUp(self) -> None:
        self.path: str = reverse("users:login")

    def test_an_authenticated_user_is_redirected(self):
        user: User = UserFactory.create()
        self.login(user)
        expected_url = reverse("users:user-preferences-update", kwargs={"pk": user.pk})
        response = self.client.get(self.path, follow=True)
        self.assertRedirects(response, expected_url)

    def test_an_unauthenticated_user_can_view_the_page(self):
        response = self.client.get(self.path)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(response, "Username")
        self.assertContains(response, "Password")

    def test_a_user_can_login_successfully(self):
        username: str = "bobby_smith"
        password: str = "S3Cr3t_P@55w0rD"

        UserFactory.create(username=username, password=password)

        form_data = {"username": username, "password": password}

        response = self.client.post(self.path, data=form_data, follow=True)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed("user_detail.html")

    def test_a_user_sees_if_they_get_username_password_combination_wrong(self):
        username: str = "bobby_smith"
        password: str = "S3Cr3t_P@55w0rD"

        UserFactory.create(username=username, password=password)

        form_data = {"username": username, "password": "wrong_password"}

        response = self.client.post(self.path, data=form_data, follow=True)

        self.assertContains(
            response,
            "Please enter a correct username and password. Note that both fields may be case-sensitive.",
        )
