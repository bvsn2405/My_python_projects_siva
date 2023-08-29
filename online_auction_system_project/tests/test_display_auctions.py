import json

import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient

client = APIClient()


@pytest.fixture()
def create_user():
    return User.objects.create_user(username="admin", password="admin", email="siva.bvsn@gmail.com")


@pytest.mark.django_db
def test_display_auctions_success(create_user):
    client.post('/online_auction/login/', data=json.dumps({"username": "admin", "password": "admin"}),
                content_type='application/json')
    data = {
        'title': 'Test Auction',
        'description': 'Test description',
        'image': "F:\\car-lamborghini-revuelto-127-641a1d518802b.jpg",
        'starting_price': 100,
        'no_of_days_auction_ends': 0,
    }
    client.post('/online_auction/create_auction/', data, format='multipart')

    response = client.get('/online_auction/display_auctions/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_display_auctions_invalid_request_method_post():
    response = client.post('/online_auction/display_auctions/')
    assert response.status_code == 405
    assert response.json() == {"message": "Invalid request method"}


@pytest.mark.django_db
def test_display_auctions_invalid_request_method_put():
    payload = json.dumps({'username': 'siva@2405',
                          'first_name': 'siva',
                          'last_name': 'b',
                          'email': 'siva@gmail.com',
                          'password': 'Siva@2405'})
    response = client.put('/online_auction/display_auctions/', payload, content_type='application/json')
    assert response.status_code == 405
    assert response.json() == {"message": "Invalid request method"}


@pytest.mark.django_db
def test_display_auctions_invalid_request_method_patch():
    payload = json.dumps({'username': 'siva@2405',
                          'first_name': 'siva',
                          'last_name': 'b',
                          'email': 'siva@gmail.com',
                          'password': 'Siva@2405'})
    response = client.patch('/online_auction/display_auctions/', payload, content_type='application/json')
    assert response.status_code == 405
    assert response.json() == {"message": "Invalid request method"}


@pytest.mark.django_db
def test_display_auctions_invalid_request_method_delete():
    payload = json.dumps({'username': 'siva@2405',
                          'first_name': 'siva',
                          'last_name': 'b',
                          'email': 'siva@gmail.com',
                          'password': 'Siva@2405'})
    response = client.delete('/online_auction/display_auctions/', payload, content_type='application/json')
    assert response.status_code == 405
    assert response.json() == {"message": "Invalid request method"}
