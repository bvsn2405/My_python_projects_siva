import json

import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient

client = APIClient()


@pytest.mark.django_db
def test_logout():
    User.objects.create_user(username='testuser', password='testpassword')
    response = client.post('/quiz/login/', json.dumps({"username": 'testuser', 'password': 'testpassword'}),
                           content_type='application/json')

    assert response.status_code == 200
    assert response.json() == {'message': "successfully logged in"}


@pytest.mark.django_db
def test_logout_with_invalid_credentials():
    User.objects.create_user(username='testuser', password='testpassword')
    response = client.post('/quiz/login/', json.dumps({"username": 'testuser1', 'password': 'testpassword'}),
                           content_type='application/json')

    assert response.status_code == 400
    assert response.json() == {'message': 'Invalid credentials'}


@pytest.mark.django_db
def test_logout_with_invalid_data():
    User.objects.create_user(username='testuser', password='testpassword')
    response = client.post('/quiz/login/', json.dumps({"username1": 'testuser1', 'password': 'testpassword'}),
                           content_type='application/json')

    assert response.status_code == 400
    assert response.json() == {'message': 'Invalid data'}


@pytest.mark.django_db
def test_logout_with_invalid_request_method():
    User.objects.create_user(username='testuser', password='testpassword')
    response = client.put('/quiz/login/', json.dumps({"username": 'testuser1', 'password': 'testpassword'}),
                           content_type='application/json')

    assert response.status_code == 400
    assert response.json() == {'message': 'Invalid request method'}




