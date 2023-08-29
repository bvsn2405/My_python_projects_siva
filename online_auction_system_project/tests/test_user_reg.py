import json

import pytest
from rest_framework.test import APIClient

client = APIClient()


@pytest.mark.django_db
def test_participants_registration_success():
    """Verifying the participants registration with correct payload"""
    payload = json.dumps({'username': 'siva@2405',
                          'first_name': 'siva',
                          'last_name': 'b',
                          'email': 'siva@gmail.com',
                          'password': 'Siva@2405'})
    response = client.post('/online_auction/user_reg/', payload, content_type='application/json')
    assert response.status_code == 200
    assert response.json() == {'message': 'user registration done successfully'}


@pytest.mark.django_db
def test_participants_registration_with_already_existing_user():
    """Verifying the participants registration with correct payload"""
    payload = json.dumps({'username': 'siva@2405',
                          'first_name': 'siva',
                          'last_name': 'b',
                          'email': 'siva@gmail.com',
                          'password': 'Siva@2405'})
    client.post('/online_auction/user_reg/', payload, content_type='application/json')
    response = client.post('/online_auction/user_reg/', payload, content_type='application/json')

    assert response.status_code == 400
    assert response.json() == {"message": "user already exists"}

@pytest.mark.django_db
def test_participants_registration_with_empty_payload():
    """Verifying the participants registration with empty payload"""
    payload = json.dumps({})
    response = client.post('/online_auction/user_reg/', payload, content_type='application/json')
    assert response.status_code == 400
    assert response.json() == {"Error message": "Invalid data submitted"}


@pytest.mark.django_db
def test_participants_registration_with_invalid_username1():
    """Verifying the participants registration with invalid username by keeping the username field empty"""
    payload = json.dumps({'username': '',
                          'first_name': 'siva',
                          'last_name': 'b',
                          'email': 'siva@gmail.com',
                          'password': 'Siva@2405'})
    response = client.post('/online_auction/user_reg/', payload, content_type='application/json')
    assert response.status_code == 400
    assert response.json() == {"Error message": ["Username should not be empty"]}


@pytest.mark.django_db
def test_participants_registration_with_invalid_username2():
    """Verifying the participants registration with invalid username by keeping the username field less than
       4 characters . """

    payload = json.dumps({'username': 'siv',
                          'first_name': 'siva',
                          'last_name': 'b',
                          'email': 'siva@gmail.com',
                          'password': 'Siva@2405'})
    response = client.post('/online_auction/user_reg/', payload, content_type='application/json')
    assert response.status_code == 400
    assert response.json() == {"Error message": ['Username should not less than 4 characters']}


@pytest.mark.django_db
def test_participants_registration_with_invalid_username3():
    """Verifying the participants registration with invalid username by keeping the username field """

    payload = json.dumps({'username': 'siva123',
                          'first_name': 'siva',
                          'last_name': 'b',
                          'email': 'siva@gmail.com',
                          'password': 'Siva@2405'})
    response = client.post('/online_auction/user_reg/', payload, content_type='application/json')
    assert response.status_code == 400
    assert response.json() == {"Error message":
                                   ['Username should contain at least one alphabet, one numeric character, and one '
                                    'special character.']}


@pytest.mark.django_db
def test_participants_registration_with_invalid_password1():
    """Verifying the participants registration with invalid password by keeping the password field as empty."""

    payload = json.dumps({'username': 'Siva@2405',
                          'first_name': 'siva',
                          'last_name': 'b',
                          'email': 'siva@gmail.com',
                          'password': ''})
    response = client.post('/online_auction/user_reg/', payload, content_type='application/json')
    assert response.status_code == 400
    assert response.json() == {"Error message": ["Password should not be empty"]}


@pytest.mark.django_db
def test_participants_registration_with_invalid_password2():
    """Verifying the participants registration with invalid password by keeping the password field less
       than 4 characters.
       """

    payload = json.dumps({'username': 'siva@123',
                          'first_name': 'siva',
                          'last_name': 'b',
                          'email': 'siva@gmail.com',
                          'password': 'Siv'})
    response = client.post('/online_auction/user_reg/', payload, content_type='application/json')
    assert response.status_code == 400
    assert response.json() == {
        "Error message": [
            "Password should not less than 4 characters"
        ]
    }


@pytest.mark.django_db
def test_participants_registration_with_invalid_password3():
    """Verifying the participants registration with invalid password """

    payload = json.dumps({'username': 'siva@123',
                          'first_name': 'siva',
                          'last_name': 'b',
                          'email': 'siva@gmail.com',
                          'password': 'Siva2405'})
    response = client.post('/online_auction/user_reg/', payload, content_type='application/json')
    assert response.status_code == 400
    assert response.json() == {
        "Error message": [
            "Password should contain at least one alphabet, one numeric character, and one special character."
        ]
    }


@pytest.mark.django_db
def test_participants_registration_invalid_request_method_get():
    """Verifying the participants registration with correct payload"""
    payload = json.dumps({'username': 'siva@2405',
                          'first_name': 'siva',
                          'last_name': 'b',
                          'email': 'siva@gmail.com',
                          'password': 'Siva@2405'})
    response = client.get('/online_auction/user_reg/')
    assert response.status_code == 405
    assert response.json() == {"message": "Invalid request method"}


@pytest.mark.django_db
def test_participants_registration_invalid_request_method_put():
    """Verifying the participants registration with correct payload"""
    payload = json.dumps({'username': 'siva@2405',
                          'first_name': 'siva',
                          'last_name': 'b',
                          'email': 'siva@gmail.com',
                          'password': 'Siva@2405'})
    response = client.put('/online_auction/user_reg/', payload, content_type='application/json')
    assert response.status_code == 405
    assert response.json() == {"message": "Invalid request method"}


@pytest.mark.django_db
def test_participants_registration_invalid_request_method_patch():
    """Verifying the participants registration with correct payload"""
    payload = json.dumps({'username': 'siva@2405',
                          'first_name': 'siva',
                          'last_name': 'b',
                          'email': 'siva@gmail.com',
                          'password': 'Siva@2405'})
    response = client.patch('/online_auction/user_reg/', payload, content_type='application/json')
    assert response.status_code == 405
    assert response.json() == {"message": "Invalid request method"}


@pytest.mark.django_db
def test_participants_registration_invalid_request_method_delete():
    """Verifying the participants registration with correct payload"""
    payload = json.dumps({'username': 'siva@2405',
                          'first_name': 'siva',
                          'last_name': 'b',
                          'email': 'siva@gmail.com',
                          'password': 'Siva@2405'})
    response = client.delete('/online_auction/user_reg/', payload, content_type='application/json')
    assert response.status_code == 405
    assert response.json() == {"message": "Invalid request method"}
