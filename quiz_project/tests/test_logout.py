import json

import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient

client = APIClient()


@pytest.mark.django_db
def test_logout():
    User.objects.create_user(username='testuser', password='testpassword')
    client.post('/quiz/login/', json.dumps({"username": 'testuser', 'password': 'testpassword'}),
                content_type='application/json')
    response = client.get('/quiz/logout/')
    assert response.status_code == 200
    assert response.json() == {'message': 'Logged out successfully'}



@pytest.mark.django_db
def test_logout_with_already_logout():
    User.objects.create_user(username='testuser', password='testpassword')
    client.post('/quiz/login/', json.dumps({"username": 'testuser', 'password': 'testpassword'}),
                content_type='application/json')
    response = client.get('/quiz/logout/')
    response = client.get('/quiz/logout/')

    assert response.status_code == 400
    assert response.json() == {'message': 'Already logged out'}