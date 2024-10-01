import pytest
from rest_framework.test import APIClient
from kittens.tests.factories import UserFactory, BreedFactory, KittenFactory

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def create_user():
    def make_user(email, password):
        return UserFactory(email=email, password=password)
    return make_user

@pytest.fixture
def auth_client(create_user, api_client):
    user = create_user('user1@example.com', 'password123')
    api_client.force_authenticate(user=user)
    return api_client

@pytest.fixture
def breed():
    return BreedFactory(name="Bengal")

@pytest.fixture
def kitten(breed, auth_client):
    return KittenFactory(owner=auth_client.handler._force_user, breed=breed)
