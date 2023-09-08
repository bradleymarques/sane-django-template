from django.core.management.base import BaseCommand
from rate_my_pet.factories import PetPictureWithCommentsAndVotesFactory

from users.factories import SuperuserFactory, UserFactory


class Command(BaseCommand):
    help = "Seeds the database for local testing"

    def handle(self, *args, **options):
        SuperuserFactory.create(
            username="superuser",
            plaintext_password="password",
            email="superuser@example.com",
        )
        UserFactory.create(
            username="user",
            plaintext_password="password",
            email="user@example.com",
        )

        for _i in range(10):
            PetPictureWithCommentsAndVotesFactory.create()
