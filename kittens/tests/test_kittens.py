import pytest
from django.urls import reverse

@pytest.mark.django_db
def test_register_user(api_client):
    url = '/users/register/'
    data = {
        'email': 'testuser@example.com',
        'password': 'password123'
    }
    response = api_client.post(url, data)
    assert response.status_code == 201
    assert response.data['email'] == 'testuser@example.com'

@pytest.mark.django_db
def test_get_breeds(api_client, breed):
    url = reverse('breed-list')
    response = api_client.get(url)
    assert response.status_code == 200
    assert len(response.data) == 1
    assert response.data[0]['name'] == 'Bengal'

@pytest.mark.django_db
def test_get_kittens(api_client, kitten):
    url = reverse('kitten-list')
    response = api_client.get(url)
    assert response.status_code == 200
    assert len(response.data) == 1
    assert response.data[0]['name'] == 'Simba'


@pytest.mark.django_db
def test_get_kittens_by_breed(api_client, kitten, breed):
    url = reverse('kitten-list')
    response = api_client.get(url, {'breed': breed.id})
    assert response.status_code == 200
    assert len(response.data) == 1
    assert response.data[0]['breed'] == breed.id

@pytest.mark.django_db
def test_get_kitten_detail(api_client, kitten):
    url = reverse('kitten-detail', args=[kitten.id])
    response = api_client.get(url)
    assert response.status_code == 200
    assert response.data['name'] == 'Simba'

@pytest.mark.django_db
def test_create_kitten(auth_client, breed):
    url = reverse('kitten-list')
    data = {
        'name': 'Simba',
        'color': 'black',
        'age': 3,
        'description': 'Playful kitten',
        'breed': breed.id
    }
    response = auth_client.post(url, data)
    assert response.status_code == 201
    assert response.data['name'] == 'Simba'
    assert response.data['breed'] == breed.id

@pytest.mark.django_db
def test_update_kitten(auth_client, kitten):
    url = reverse('kitten-detail', args=[kitten.id])
    data = {
        'name': 'Simba Updated',
        'color': 'black',
        'age': 4,
        'description': 'Updated description',
        'breed': kitten.breed.id
    }
    response = auth_client.put(url, data)
    assert response.status_code == 200
    assert response.data['name'] == 'Simba Updated'
    assert response.data['description'] == 'Updated description'

@pytest.mark.django_db
def test_delete_kitten(auth_client, kitten):
    url = reverse('kitten-detail', args=[kitten.id])
    response = auth_client.delete(url)
    assert response.status_code == 204

@pytest.mark.django_db
def test_rate_kitten(auth_client, kitten):
    url = '/ratings/'
    data = {
        'kitten': kitten.id,
        'score': 5
    }
    response = auth_client.post(url, data)
    assert response.status_code == 201
    assert response.data['score'] == 5


@pytest.mark.django_db
def test_average_rating(api_client, kitten, auth_client):
    url = '/ratings/'
    data = {
        'kitten': kitten.id,
        'score': 5
    }
    response = auth_client.post(url, data)
    assert response.status_code == 201

    url = f'/kittens/{kitten.id}/'
    response = api_client.get(url)
    assert response.status_code == 200
    assert response.data['average_rating'] == 5.0