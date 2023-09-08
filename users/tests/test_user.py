from core.tests import BaseTest
from users.factories import SuperuserFactory, UserFactory
from users.models import User


class TestUser(BaseTest):
    def test_the_factory_produces_a_valid_user(self):
        user: User = UserFactory.create()
        self.assertIsNotNone(user.username)
        self.assertIsNotNone(user.email)
        self.assertIsNotNone(user.first_name)
        self.assertIsNotNone(user.last_name)

    def test_the_factory_produces_a_user_with_the_provided_details(self):
        user: User = UserFactory.create(
            username="elongated_muskrat",
            email="elongatedmuskrat@example.com",
            first_name="Elongated",
            last_name="Muskrat",
            plaintext_password="M@rsRuL3Z!",
        )

        self.assertEqual(user.username, "elongated_muskrat")
        self.assertEqual(user.email, "elongatedmuskrat@example.com")
        self.assertEqual(user.first_name, "Elongated")
        self.assertEqual(user.last_name, "Muskrat")

    def test_superuser_factory_produces_a_valid_user(self):
        user: User = UserFactory.create()
        super_user: User = SuperuserFactory.create()
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        self.assertTrue(super_user.is_staff)
        self.assertTrue(super_user.is_superuser)
