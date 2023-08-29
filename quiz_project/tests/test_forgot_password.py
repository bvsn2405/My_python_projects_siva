import json
import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient

client = APIClient()


@pytest.fixture()
def create_user():
    User.objects.create_user(username="testuser", password="testpassword", email="siva.iiit@gmail.com")



@pytest.mark.django_db
def test_forgot_password_success(create_user):

    """Verifying forgot password functionality with all valid data"""
    data = {"username": "testuser"}

    response = client.post('/quiz/forgot_password/', json.dumps(data), content_type='application/json')
    assert response.status_code == 200
    assert response.json() == {"message": "OTP sent to your mail successfully"}


@pytest.mark.django_db
def test_forgot_password_invalid_data():

    """Verifying forgot password functionality with invalid data"""
    data = {"username": "testuser"}

    response = client.post('/quiz/forgot_password/', json.dumps(data), content_type='application/json')
    assert response.status_code == 400
    assert response.json() == {"message": "User does not exist"}


@pytest.mark.django_db
def test_forgot_password_invalid_data2():

    """Verifying forgot password functionality with invalid data"""
    data = {"usernameww": "tekstuser"}

    response = client.post('/quiz/forgot_password/', json.dumps(data), content_type='application/json')
    assert response.status_code == 400
    assert response.json() == {"message": "Invalid data"}


@pytest.mark.django_db
def test_forgot_password_invalid_data3():

    """Verifying forgot password functionality with empty payload"""
    data = {}

    response = client.post('/quiz/forgot_password/', json.dumps(data), content_type='application/json')
    assert response.status_code == 400
    assert response.json() == {"message": "Invalid data"}


@pytest.mark.django_db
def test_forgot_password_invalid_request_method():

    """Verifying forgot password functionality with empty payload"""

    response = client.get('/quiz/forgot_password/',content_type='application/json')
    assert response.status_code == 400
    assert response.json() == {"message": "Invalid request method"}
