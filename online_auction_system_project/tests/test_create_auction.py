import json

import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient

client = APIClient()


@pytest.fixture()
def create_user():
    return User.objects.create_user(username="admin", password="admin", email="siva.bvsn@gmail.com")


@pytest.mark.django_db(transaction=True)
def test_create_user_success(create_user):
    client.post('/online_auction/login/', data=json.dumps({"username": "admin", "password": "admin"}),
                content_type='application/json')
    data = {
        'title': 'Test Auction',
        'description': 'Test description',
        'image': "F:\\car-lamborghini-revuelto-127-641a1d518802b.jpg",
        'starting_price': 100,
        'no_of_days_auction_ends': 3,
    }
    response = client.post('/online_auction/create_auction/', data, format='multipart')
    assert response.status_code == 200
    assert response.json() == {"message": "Auction created successfully !"}


@pytest.mark.django_db(transaction=True)
def test_create_user_invalid_data(create_user):
    client.post('/online_auction/login/', data=json.dumps({"username": "admin", "password": "admin"}),
                content_type='application/json')
    data = {
        'description1': 'Test description',
        'image': "F:\\car-lamborghini-revuelto-127-641a1d518802b.jpg",
        'starting_price': 100,
        'no_of_days_auction_ends': 3,
    }
    response = client.post('/online_auction/create_auction/', data, format='multipart')
    assert response.status_code == 400


@pytest.mark.django_db(transaction=True)
def test_create_user_without_authorizing():
    data = {
        'description1': 'Test description',
        'image': "F:\\car-lamborghini-revuelto-127-641a1d518802b.jpg",
        'starting_price': 100,
        'no_of_days_auction_ends': 3,
    }
    response = client.post('/online_auction/create_auction/', data, format='multipart')
    assert response.status_code == 400
    assert response.json() == {"message": "User is not authenticated"}



@pytest.mark.django_db(transaction=True)
def test_create_user_invalid_request_method_get(create_user):
    client.post('/online_auction/login/', data=json.dumps({"username": "admin", "password": "admin"}),
                content_type='application/json')
    data = {
        'title': 'Test Auction',
        'description': 'Test description',
        'image': "F:\\car-lamborghini-revuelto-127-641a1d518802b.jpg",
        'starting_price': 100,
        'no_of_days_auction_ends': 3,
    }
    response = client.get('/online_auction/create_auction/')
    assert response.status_code == 405
    assert response.json() == {"message": "Invalid request method"}


@pytest.mark.django_db(transaction=True)
def test_create_user_invalid_request_method_put(create_user):
    client.post('/online_auction/login/', data=json.dumps({"username": "admin", "password": "admin"}),
                content_type='application/json')
    data = {
        'title': 'Test Auction',
        'description': 'Test description',
        'image': "F:\\car-lamborghini-revuelto-127-641a1d518802b.jpg",
        'starting_price': 100,
        'no_of_days_auction_ends': 3,
    }
    response = client.put('/online_auction/create_auction/', data, format='multipart')
    assert response.status_code == 405
    assert response.json() == {"message": "Invalid request method"}


@pytest.mark.django_db(transaction=True)
def test_create_user_invalid_request_method_patch(create_user):
    client.post('/online_auction/login/', data=json.dumps({"username": "admin", "password": "admin"}),
                content_type='application/json')
    data = {
        'title': 'Test Auction',
        'description': 'Test description',
        'image': "F:\\car-lamborghini-revuelto-127-641a1d518802b.jpg",
        'starting_price': 100,
        'no_of_days_auction_ends': 3,
    }
    response = client.patch('/online_auction/create_auction/', data, format='multipart')
    assert response.status_code == 405
    assert response.json() == {"message": "Invalid request method"}


@pytest.mark.django_db(transaction=True)
def test_create_user_invalid_request_method_delete(create_user):
    client.post('/online_auction/login/', data=json.dumps({"username": "admin", "password": "admin"}),
                content_type='application/json')
    data = {
        'title': 'Test Auction',
        'description': 'Test description',
        'image': "F:\\car-lamborghini-revuelto-127-641a1d518802b.jpg",
        'starting_price': 100,
        'no_of_days_auction_ends': 3,
    }
    response = client.delete('/online_auction/create_auction/', data, format='multipart')
    assert response.status_code == 405
    assert response.json() == {"message": "Invalid request method"}