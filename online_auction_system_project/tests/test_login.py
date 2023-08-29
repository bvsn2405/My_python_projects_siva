import json

import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient

client = APIClient()


@pytest.mark.django_db
def test_login():
    User.objects.create_user(username='testuser', password='testpassword')
    response = client.post('/online_auction/login/', json.dumps({"username": 'testuser', 'password': 'testpassword'}),
                           content_type='application/json')

    assert response.status_code == 200
    assert response.json() == {'message': "successfully logged in"}


@pytest.mark.django_db
def test_login_with_invalid_credentials():
    User.objects.create_user(username='testuser', password='testpassword')
    response = client.post('/online_auction/login/', json.dumps({"username": 'testuser1', 'password': 'testpassword'}),
                           content_type='application/json')

    assert response.status_code == 400
    assert response.json() == {'message': 'Invalid credentials'}


@pytest.mark.django_db
def test_login_with_invalid_data():
    User.objects.create_user(username='testuser', password='testpassword')
    response = client.post('/online_auction/login/', json.dumps({"username1": 'testuser1', 'password': 'testpassword'}),
                           content_type='application/json')

    assert response.status_code == 400
    assert response.json() == {'message': 'Invalid data provided'}


@pytest.mark.django_db
def test_login_with_invalid_request_method_get():
    User.objects.create_user(username='testuser', password='testpassword')
    response = client.get('/online_auction/login/')

    assert response.status_code == 405
    assert response.json() == {"message": "Invalid request method"}


@pytest.mark.django_db
def test_login_with_invalid_request_method_put():
    User.objects.create_user(username='testuser', password='testpassword')
    response = client.put('/online_auction/login/', json.dumps({"username": 'testuser', 'password': 'testpassword'}),
                           content_type='application/json')

    assert response.status_code == 405
    assert response.json() == {"message": "Invalid request method"}


@pytest.mark.django_db
def test_login_with_invalid_request_method_patch():
    User.objects.create_user(username='testuser', password='testpassword')
    response = client.patch('/online_auction/login/', json.dumps({"username": 'testuser', 'password': 'testpassword'}),
                           content_type='application/json')

    assert response.status_code == 405
    assert response.json() == {"message": "Invalid request method"}


@pytest.mark.django_db
def test_login_with_invalid_request_method_delete():
    User.objects.create_user(username='testuser', password='testpassword')
    response = client.delete('/online_auction/login/', json.dumps({"username": 'testuser', 'password': 'testpassword'}),
                           content_type='application/json')

    assert response.status_code == 405
    assert response.json() == {"message": "Invalid request method"}

