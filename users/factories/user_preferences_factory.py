import factory
import factory.fuzzy

from users.factories.user_factory import UserFactory
from users.objects.theme import DEFAULT_THEME


class UserPreferencesFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "users.UserPreferences"
        django_get_or_create = ()

    user = factory.SubFactory(UserFactory)
    theme = DEFAULT_THEME

    profile_picture = factory.django.ImageField(
        from_path=factory.fuzzy.FuzzyChoice(
            [
                "users/sample_pictures/profile_1.jpg",
                "users/sample_pictures/profile_2.jpg",
                "users/sample_pictures/profile_3.jpg",
                "users/sample_pictures/profile_4.jpg",
                "users/sample_pictures/profile_5.jpg",
            ]
        )
    )
