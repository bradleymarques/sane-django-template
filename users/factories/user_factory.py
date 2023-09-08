import factory
import factory.fuzzy


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "users.User"
        django_get_or_create = ()
        skip_postgeneration_save = False

    username = factory.Faker("user_name")
    email = factory.Faker("email")
    first_name = ""
    last_name = ""

    plaintext_password = factory.PostGenerationMethodCall("set_password", "password")

    is_superuser = False
    is_staff = False
    is_active = True

    user_preferences = factory.RelatedFactory(
        "users.factories.UserPreferencesFactory",
        factory_related_name="user",
    )

    @classmethod
    def _after_postgeneration(cls, instance, create, results=None):
        instance.save()
