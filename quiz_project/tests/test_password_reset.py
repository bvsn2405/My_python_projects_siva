import json

import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient

client = APIClient()


@pytest.fixture()
def create_user():
    User.objects.create_user(username="testuser", password="testpassword", email="siva.iiit@gmail.com")



@pytest.mark.django_db
def test_password_reset_success(create_user):

    """Verifying password reset functionality with all valid data"""
    data = {"username": "testuser", "password": "testpassword"}
    client.post('/quiz/login/', json.dumps(data), content_type='application/json')

    data = {"new_password": "Password@123"}
    response = client.post('/quiz/password_reset/', json.dumps(data), content_type='application/json')
    assert response.status_code == 200
    assert response.json() == {"message": "password updated successfully ! "}


@pytest.mark.django_db
def test_password_rest_without_authorizing(create_user):
    """Verifying password reset functionality with all valid data and unauthorized user"""
    data = {"new_password": "Password@123"}
    response = client.post('/quiz/password_reset/', json.dumps(data), content_type='application/json')
    assert response.status_code == 400
    assert response.json() == {
        "message": "User is not authenticated"
    }


@pytest.mark.django_db
def test_password_rest_with_invalid_data_authorizing(create_user):
    """Verifying password reset functionality with all valid data and authorized user"""
    data = {"username": "testuser", "password": "testpassword"}
    client.post('/quiz/login/', json.dumps(data), content_type='application/json')
    data = {"new_password1": "Password@123"}
    response = client.post('/quiz/password_reset/', json.dumps(data), content_type='application/json')
    assert response.status_code == 400
    assert response.json() == {"message": "Invalid data provided !"}


@pytest.mark.django_db
def test_password_rest_with_invalid_data_authorizing_2(create_user):
    """Verifying password reset functionality with empty payload and unauthorized user"""
    data = {"username": "testuser", "password": "testpassword"}
    client.post('/quiz/login/', json.dumps(data), content_type='application/json')
    data = {}
    response = client.post('/quiz/password_reset/', json.dumps(data), content_type='application/json')
    assert response.status_code == 400
    assert response.json() == {"message": "Invalid data provided !"}


@pytest.mark.django_db
def test_password_rest_with_invalid_request_method(create_user):
    """Verifying password reset functionality with empty payload and unauthorized user"""
    data = {"username": "testuser", "password": "testpassword"}
    client.post('/quiz/login/', json.dumps(data), content_type='application/json')
    data = {}
    response = client.get('/quiz/password_reset/',content_type='application/json')
    assert response.status_code == 400
    assert response.json() == {"message": "Invalid request method"}