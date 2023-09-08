from http import HTTPStatus

from django.urls import reverse

from core.tests.base_test import BaseTest
from users.factories import UserFactory
from users.models import User


class TestUserDetailView(BaseTest):
    def setUp(self) -> None:
        self.user: User = UserFactory.create()
        self.path = reverse("users:users-detail", kwargs={"pk": self.user.pk})

    def test_an_unauthenticated_user_cannot_view_the_page(self):
        self.assert_unauthenticated_get(self.path)

    def test_a_user_cannot_view_another_users_page(self):
        another_user: User = UserFactory.create()
        self.login(another_user)
        self.assert_unauthorized_get(self.path)

    def test_a_user_can_view_their_own_page(self):
        self.login(self.user)
        response = self.client.get(self.path)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed("user_detail.html")
        self.assertContains(response, self.user.__str__())
