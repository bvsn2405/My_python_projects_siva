import json

import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient

client = APIClient()


@pytest.mark.django_db
def test_logout():
    User.objects.create_user(username='testuser', password='testpassword')
    client.post('/online_auction/login/', json.dumps({"username": 'testuser', 'password': 'testpassword'}),
                content_type='application/json')
    response = client.get('/online_auction/logout/')
    assert response.status_code == 200
    assert response.json() == {'message': 'Logged out successfully'}



@pytest.mark.django_db
def test_logout_with_already_logout():
    User.objects.create_user(username='testuser', password='testpassword')
    client.post('/online_auction/login/', json.dumps({"username": 'testuser', 'password': 'testpassword'}),
                content_type='application/json')
    client.get('/online_auction/logout/')
    response = client.get('/online_auction/logout/')

    assert response.status_code == 400
    assert response.json() == {'message': 'Already logged out'}


@pytest.mark.django_db
def test_logout_with_invalid_request_method_post():
    response = client.post('/online_auction/logout/')

    assert response.status_code == 405
    assert response.json() == {"message": "Invalid request method"}


@pytest.mark.django_db
def test_logout_with_invalid_request_method_put():
    response = client.put('/online_auction/logout/')

    assert response.status_code == 405
    assert response.json() == {"message": "Invalid request method"}


@pytest.mark.django_db
def test_logout_with_invalid_request_method_patch():
    User.objects.create_user(username='testuser', password='testpassword')
    response = client.patch('/online_auction/logout/')

    assert response.status_code == 405
    assert response.json() == {"message": "Invalid request method"}


@pytest.mark.django_db
def test_logout_with_invalid_request_method_delete():
    response = client.delete('/online_auction/logout/')

    assert response.status_code == 405
    assert response.json() == {"message": "Invalid request method"}

