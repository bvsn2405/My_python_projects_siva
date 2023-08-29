import json

import pytest
from rest_framework.test import APIClient

client = APIClient()


@pytest.mark.django_db(transaction=True)
def test_participants_update_put_method_success():
    """Verifying the participants registration with correct payload"""
    payload = json.dumps({'username': 'admin@123',
                          'first_name': 'siva',
                          'last_name': 'b',
                          'email': 'siva@gmail.com',
                          'password': 'admin@123'})
    response = client.post('/quiz/participants/reg/', payload, content_type='application/json')
    assert response.json() == {'message': 'user registration done successfully'}

    response = client.post('/quiz/login/', json.dumps({"username": 'admin@123', "password": 'admin@123'}),
                           content_type='application/json')
    assert response.json() == {'message': 'successfully logged in'}

    update_data = {
        'username': 'siva@123',
        'first_name': 'siva',
        'last_name': 'b',
        'email': 'siva@gmail.com',
        'password': 'Siva@123'
    }
    response = client.put('/quiz/participants/update/', json.dumps(update_data), content_type='application/json')

    # assert response.status_code == 200
    assert response.json() == {'message': 'User data updated successfully'}


@pytest.mark.django_db(transaction=True)
def test_participants_update_put_method_invalid_data():
    """Verifying the participants registration with correct payload"""
    payload = json.dumps({'username': 'admin@123',
                          'first_name': 'siva',
                          'last_name': 'b',
                          'email': 'siva@gmail.com',
                          'password': 'admin@123'})
    response = client.post('/quiz/participants/reg/', payload, content_type='application/json')
    assert response.json() == {'message': 'user registration done successfully'}

    response = client.post('/quiz/login/', json.dumps({"username": 'admin@123', "password": 'admin@123'}),
                           content_type='application/json')
    assert response.json() == {'message': 'successfully logged in'}

    update_data = {
        'username1': 'siva@123',
        'first_name': 'siva',
        'last_name': 'b',
        'email': 'siva@gmail.com',
        'password': 'Siva@123'
    }
    response = client.put('/quiz/participants/update/', json.dumps(update_data), content_type='application/json')

    assert response.status_code == 400
    assert response.json() == {'message': 'Invalid Data'}


@pytest.mark.django_db(transaction=True)
def test_participants_update_put_method_invalid_data_2():
    """Verifying the participants registration with correct payload"""
    payload = json.dumps({'username': 'admin@123',
                          'first_name': 'siva',
                          'last_name': 'b',
                          'email': 'siva@gmail.com',
                          'password': 'admin@123'})
    response = client.post('/quiz/participants/reg/', payload, content_type='application/json')
    assert response.json() == {'message': 'user registration done successfully'}

    response = client.post('/quiz/login/', json.dumps({"username": 'admin@123', "password": 'admin@123'}),
                           content_type='application/json')
    assert response.json() == {'message': 'successfully logged in'}

    update_data = {
        'username': 'siva',
        'first_name': 'siva',
        'last_name': 'b',
        'email': 'siva@gmail.com',
        'password': 'Siva@123'
    }
    response = client.put('/quiz/participants/update/', json.dumps(update_data), content_type='application/json')

    assert response.status_code == 400
    assert response.json() == {'Error message': [
        'Username should contain at least one alphabet, one numeric character, and one special character.']}


@pytest.mark.django_db(transaction=True)
def test_participants_update_put_method_invalid_data_3():
    """Verifying the participants registration with correct payload"""
    payload = json.dumps({'username': 'admin@123',
                          'first_name': 'siva',
                          'last_name': 'b',
                          'email': 'siva@gmail.com',
                          'password': 'admin@123'})
    response = client.post('/quiz/participants/reg/', payload, content_type='application/json')
    assert response.json() == {'message': 'user registration done successfully'}

    response = client.post('/quiz/login/', json.dumps({"username": 'admin@123', "password": 'admin@123'}),
                           content_type='application/json')
    assert response.json() == {'message': 'successfully logged in'}

    update_data = {
        'username': 'siva@123',
        'first_name': 'siva',
        'last_name': 'b',
        'email': 'siva@gmail.com',
        'password': 'Siva'
    }
    response = client.put('/quiz/participants/update/', json.dumps(update_data), content_type='application/json')

    assert response.status_code == 400
    assert response.json() == {'Error message': [
        'Password should contain at least one alphabet, one numeric character, and one special character.']}


@pytest.mark.django_db(transaction=True)
def test_participants_update_put_method_invalid_data_4():
    """Verifying the participants registration with correct payload"""
    payload = json.dumps({'username': 'admin@123',
                          'first_name': 'siva',
                          'last_name': 'b',
                          'email': 'siva@gmail.com',
                          'password': 'admin@123'})
    response = client.post('/quiz/participants/reg/', payload, content_type='application/json')
    assert response.json() == {'message': 'user registration done successfully'}

    response = client.post('/quiz/login/', json.dumps({"username": 'admin@123', "password": 'admin@123'}),
                           content_type='application/json')
    assert response.json() == {'message': 'successfully logged in'}

    update_data = {
        'username': 'siva',
        'first_name': 'siva',
        'last_name': 'b',
        'email': 'siva@gmail.com',
        'password': 'Siva'
    }
    response = client.put('/quiz/participants/update/', json.dumps(update_data), content_type='application/json')

    assert response.status_code == 400
    assert response.json() == {'Error message': [
        'Username should contain at least one alphabet, one numeric character, and one special character.',
        'Password should contain at least one alphabet, one numeric character, and one special character.']}


@pytest.mark.django_db(transaction=True)
def test_participants_update_put_method_invalid_data_5():
    """Verifying the participants registration with correct payload"""
    payload = json.dumps({'username': 'admin@123',
                          'first_name': 'siva',
                          'last_name': 'b',
                          'email': 'siva@gmail.com',
                          'password': 'admin@123'})
    response = client.post('/quiz/participants/reg/', payload, content_type='application/json')
    assert response.json() == {'message': 'user registration done successfully'}

    response = client.post('/quiz/login/', json.dumps({"username": 'admin@123', "password": 'admin@123'}),
                           content_type='application/json')
    assert response.json() == {'message': 'successfully logged in'}

    update_data = {
        'username': '',
        'first_name': 'siva',
        'last_name': 'b',
        'email': 'siva@gmail.com',
        'password': ''
    }
    response = client.put('/quiz/participants/update/', json.dumps(update_data), content_type='application/json')

    assert response.status_code == 400
    assert response.json() == {
        "Error message": [
            "Username should not be empty",
            "Password should not be empty"
        ]
    }


@pytest.mark.django_db(transaction=True)
def test_participants_update_put_method_invalid_data_6():
    """Verifying the participants registration with correct payload"""
    payload = json.dumps({'username': 'admin@123',
                          'first_name': 'siva',
                          'last_name': 'b',
                          'email': 'siva@gmail.com',
                          'password': 'admin@123'})
    response = client.post('/quiz/participants/reg/', payload, content_type='application/json')
    assert response.json() == {'message': 'user registration done successfully'}

    response = client.post('/quiz/login/', json.dumps({"username": 'admin@123', "password": 'admin@123'}),
                           content_type='application/json')
    assert response.json() == {'message': 'successfully logged in'}

    update_data = {}
    response = client.put('/quiz/participants/update/', json.dumps(update_data), content_type='application/json')

    assert response.status_code == 400
    assert response.json() == {"message": "Invalid Data"}


@pytest.mark.django_db(transaction=True)
def test_participants_update_put_method_with_unauthorized_user():
    """Verifying the participants registration with correct payload"""
    update_data = {}
    response = client.put('/quiz/participants/update/', json.dumps(update_data), content_type='application/json')

    assert response.status_code == 400
    assert response.json() == {'message': 'User is not authenticated'}


@pytest.mark.django_db(transaction=True)
def test_participants_update_patch_method_success():
    """Verifying the participants registration with correct payload"""
    payload = json.dumps({'username': 'admin@123',
                          'first_name': 'siva',
                          'last_name': 'b',
                          'email': 'siva@gmail.com',
                          'password': 'admin@123'})
    response = client.post('/quiz/participants/reg/', payload, content_type='application/json')
    assert response.json() == {'message': 'user registration done successfully'}

    response = client.post('/quiz/login/', json.dumps({"username": 'admin@123', "password": 'admin@123'}),
                           content_type='application/json')
    assert response.json() == {'message': 'successfully logged in'}

    update_data = {
        'username': 'siva@1234',
        'first_name': 'siva'
    }
    response = client.patch('/quiz/participants/update/', json.dumps(update_data), content_type='application/json')

    assert response.status_code == 200
    assert response.json() == {'message': 'User Data updated successfully'}


@pytest.mark.django_db(transaction=True)
def test_participants_update_patch_method_success_1():
    """Verifying the participants registration with correct payload"""
    payload = json.dumps({'username': 'admin@123',
                          'first_name': 'siva',
                          'last_name': 'b',
                          'email': 'siva@gmail.com',
                          'password': 'admin@123'})
    response = client.post('/quiz/participants/reg/', payload, content_type='application/json')
    assert response.json() == {'message': 'user registration done successfully'}

    response = client.post('/quiz/login/', json.dumps({"username": 'admin@123', "password": 'admin@123'}),
                           content_type='application/json')
    assert response.json() == {'message': 'successfully logged in'}

    update_data = {
        'password': 'admin@123'}

    response = client.patch('/quiz/participants/update/', json.dumps(update_data), content_type='application/json')

    assert response.status_code == 200
    assert response.json() == {'message': 'User Data updated successfully'}


@pytest.mark.django_db(transaction=True)
def test_participants_update_patch_method_success_2():
    """Verifying the participants registration with correct payload"""
    payload = json.dumps({'username': 'admin@123',
                          'first_name': 'siva',
                          'last_name': 'b',
                          'email': 'siva@gmail.com',
                          'password': 'admin@123'})
    response = client.post('/quiz/participants/reg/', payload, content_type='application/json')
    assert response.json() == {'message': 'user registration done successfully'}

    response = client.post('/quiz/login/', json.dumps({"username": 'admin@123', "password": 'admin@123'}),
                           content_type='application/json')
    assert response.json() == {'message': 'successfully logged in'}

    update_data = {'first_name': 'siva',
                   'last_name': 'b',
                   'email': 'siva@gmail.com'}

    response = client.patch('/quiz/participants/update/', json.dumps(update_data), content_type='application/json')

    assert response.status_code == 200
    assert response.json() == {'message': 'User Data updated successfully'}


@pytest.mark.django_db(transaction=True)
def test_participants_update_patch_method_invalid_data():
    """Verifying the participants registration with correct payload"""
    payload = json.dumps({'username': 'admin@123',
                          'first_name': 'siva',
                          'last_name': 'b',
                          'email': 'siva@gmail.com',
                          'password': 'admin@123'})
    response = client.post('/quiz/participants/reg/', payload, content_type='application/json')
    assert response.json() == {'message': 'user registration done successfully'}

    response = client.post('/quiz/login/', json.dumps({"username": 'admin@123', "password": 'admin@123'}),
                           content_type='application/json')
    assert response.json() == {'message': 'successfully logged in'}

    update_data = {
        'username1': 'siva@123',

    }
    response = client.patch('/quiz/participants/update/', json.dumps(update_data), content_type='application/json')

    assert response.status_code == 400
    assert response.json() == {'message': 'Invalid Data'}


@pytest.mark.django_db(transaction=True)
def test_participants_update_patch_method_invalid_data_2():
    """Verifying the participants registration with correct payload"""
    payload = json.dumps({'username': 'admin@123',
                          'first_name': 'siva',
                          'last_name': 'b',
                          'email': 'siva@gmail.com',
                          'password': 'admin@123'})
    response = client.post('/quiz/participants/reg/', payload, content_type='application/json')
    assert response.json() == {'message': 'user registration done successfully'}

    response = client.post('/quiz/login/', json.dumps({"username": 'admin@123', "password": 'admin@123'}),
                           content_type='application/json')
    assert response.json() == {'message': 'successfully logged in'}

    update_data = {
        'username': 'siva',
        'first_name': 'siva',
        'last_name': 'b',
        'email': 'siva@gmail.com',
        'password': 'Siva@123'
    }
    response = client.patch('/quiz/participants/update/', json.dumps(update_data), content_type='application/json')

    assert response.status_code == 400
    assert response.json() == {'Error message': [
        'Username should contain at least one alphabet, one numeric character, and one special character.']}


@pytest.mark.django_db(transaction=True)
def test_participants_update_patch_method_invalid_data_3():
    """Verifying the participants registration with correct payload"""
    payload = json.dumps({'username': 'admin@123',
                          'first_name': 'siva',
                          'last_name': 'b',
                          'email': 'siva@gmail.com',
                          'password': 'admin@123'})
    response = client.post('/quiz/participants/reg/', payload, content_type='application/json')
    assert response.json() == {'message': 'user registration done successfully'}

    response = client.post('/quiz/login/', json.dumps({"username": 'admin@123', "password": 'admin@123'}),
                           content_type='application/json')
    assert response.json() == {'message': 'successfully logged in'}

    update_data = {
        'username': 'siva@123',
        'first_name': 'siva',
        'last_name': 'b',
        'email': 'siva@gmail.com',
        'password': 'Siva'
    }
    response = client.patch('/quiz/participants/update/', json.dumps(update_data), content_type='application/json')

    assert response.status_code == 400
    assert response.json() == {'Error message': [
        'Password should contain at least one alphabet, one numeric character, and one special character.']}


@pytest.mark.django_db(transaction=True)
def test_participants_update_patch_method_invalid_data_4():
    """Verifying the participants registration with correct payload"""
    payload = json.dumps({'username': 'admin@123',
                          'first_name': 'siva',
                          'last_name': 'b',
                          'email': 'siva@gmail.com',
                          'password': 'admin@123'})
    response = client.post('/quiz/participants/reg/', payload, content_type='application/json')
    assert response.json() == {'message': 'user registration done successfully'}

    response = client.post('/quiz/login/', json.dumps({"username": 'admin@123', "password": 'admin@123'}),
                           content_type='application/json')
    assert response.json() == {'message': 'successfully logged in'}

    update_data = {
        'username': 'siva',
        'first_name': 'siva',
        'last_name': 'b',
        'email': 'siva@gmail.com',
        'password': 'Siva'
    }
    response = client.patch('/quiz/participants/update/', json.dumps(update_data), content_type='application/json')

    assert response.status_code == 400
    assert response.json() == {'Error message': [
        'Username should contain at least one alphabet, one numeric character, and one special character.',
        'Password should contain at least one alphabet, one numeric character, and one special character.']}


@pytest.mark.django_db(transaction=True)
def test_participants_update_patch_method_invalid_data_5():
    """Verifying the participants registration with correct payload"""
    payload = json.dumps({'username': 'admin@123',
                          'first_name': 'siva',
                          'last_name': 'b',
                          'email': 'siva@gmail.com',
                          'password': 'admin@123'})
    response = client.post('/quiz/participants/reg/', payload, content_type='application/json')
    assert response.json() == {'message': 'user registration done successfully'}

    response = client.post('/quiz/login/', json.dumps({"username": 'admin@123', "password": 'admin@123'}),
                           content_type='application/json')
    assert response.json() == {'message': 'successfully logged in'}

    update_data = {
        'username': '',
        'first_name': 'siva',
        'last_name': 'b',
        'email': 'siva@gmail.com',
        'password': ''
    }
    response = client.patch('/quiz/participants/update/', json.dumps(update_data), content_type='application/json')

    assert response.status_code == 400
    assert response.json() == {
        "Error message": [
            "Username should not be empty",
            "Password should not be empty"
        ]
    }


@pytest.mark.django_db(transaction=True)
def test_participants_update_patch_method_invalid_data_6():
    """Verifying the participants registration with correct payload"""
    payload = json.dumps({'username': 'admin@123',
                          'first_name': 'siva',
                          'last_name': 'b',
                          'email': 'siva@gmail.com',
                          'password': 'admin@123'})
    response = client.post('/quiz/participants/reg/', payload, content_type='application/json')
    assert response.json() == {'message': 'user registration done successfully'}

    response = client.post('/quiz/login/', json.dumps({"username": 'admin@123', "password": 'admin@123'}),
                           content_type='application/json')
    assert response.json() == {'message': 'successfully logged in'}

    update_data = {}
    response = client.patch('/quiz/participants/update/', json.dumps(update_data), content_type='application/json')

    assert response.status_code == 400
    assert response.json() == {"message": "Invalid Data"}


@pytest.mark.django_db(transaction=True)
def test_participants_update_patch_method_with_unauthorized_user():
    """Verifying the participants registration with correct payload"""
    update_data = {}
    response = client.patch('/quiz/participants/update/', json.dumps(update_data), content_type='application/json')

    assert response.status_code == 400
    assert response.json() == {'message': 'User is not authenticated'}


@pytest.mark.django_db(transaction=True)
def test_participants_update_invalid_request_method():
    """Verifying the participants registration with correct payload"""
    payload = json.dumps({'username': 'admin@123',
                          'first_name': 'siva',
                          'last_name': 'b',
                          'email': 'siva@gmail.com',
                          'password': 'admin@123'})
    response = client.post('/quiz/participants/reg/', payload, content_type='application/json')
    assert response.json() == {'message': 'user registration done successfully'}

    response = client.post('/quiz/login/', json.dumps({"username": 'admin@123', "password": 'admin@123'}),
                           content_type='application/json')
    assert response.json() == {'message': 'successfully logged in'}

    update_data = {}
    response = client.post('/quiz/participants/update/', json.dumps(update_data), content_type='application/json')

    assert response.status_code == 400
    assert response.json() == {"Message": "Invalid request method"}
