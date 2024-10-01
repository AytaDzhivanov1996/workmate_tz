import factory
from users.models import User
from kittens.models import Kitten, Breed


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
        skip_postgeneration_save = True

    email = factory.Sequence(lambda n: f"user{n}@example.com")
    password = factory.PostGenerationMethodCall('set_password', 'password123')

class BreedFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Breed

    name = "Bengal"

class KittenFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Kitten

    name = "Simba"
    color = "black"
    age = 3
    description = "A playful Bengal kitten"
    breed = factory.SubFactory(BreedFactory)
    owner = factory.SubFactory(UserFactory)
