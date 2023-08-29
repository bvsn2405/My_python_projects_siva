import json

import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient

client = APIClient()


@pytest.fixture
def participants():
    return User.objects.create_user(username='testuser', password='testpassword'), User.objects.create_user(
        username='testuser1', password='testpassword')


@pytest.mark.django_db(transaction=True)
def test_get_feedbacks_success(participants):
    client.post('/quiz/login/', json.dumps({'username': 'testuser', 'password': 'testpassword'}),
                content_type='application/json')
    data = {"feedback": "Testing the feedback functionality"}
    client.post('/quiz/submit_feedback/', json.dumps(data), content_type='application/json')

    response = client.get('/quiz/feedbacks/')
    assert response.status_code == 200


@pytest.mark.django_db(transaction=True)
def test_get_feedbacks_invalid_request_method(participants):
    client.post('/quiz/login/', json.dumps({'username': 'testuser', 'password': 'testpassword'}),
                content_type='application/json')
    data = {"feedback": "Testing the feedback functionality"}
    client.post('/quiz/submit_feedback/', json.dumps(data), content_type='application/json')

    response = client.delete('/quiz/feedbacks/')
    assert response.status_code == 400
    assert response.json() == {"message": "Invalid request method"}


@pytest.mark.django_db(transaction=True)
def test_get_feedback_success(participants):
    client.post('/quiz/login/', json.dumps({'username': 'testuser', 'password': 'testpassword'}),
                content_type='application/json')
    data = {"feedback": "Testing the feedback functionality"}
    client.post('/quiz/submit_feedback/', json.dumps(data), content_type='application/json')

    response = client.get('/quiz/feedback/1/')
    assert response.status_code == 200


@pytest.mark.django_db(transaction=True)
def test_get_feedback_invalid_request_method(participants):
    client.post('/quiz/login/', json.dumps({'username': 'testuser', 'password': 'testpassword'}),
                content_type='application/json')
    data = {"feedback": "Testing the feedback functionality"}
    client.post('/quiz/submit_feedback/', json.dumps(data), content_type='application/json')

    response = client.delete('/quiz/feedback/1/')
    assert response.status_code == 400
    assert response.json() == {"message": "Invalid request method"}


@pytest.mark.django_db(transaction=True)
def test_get_feedback_success(participants):
    client.post('/quiz/login/', json.dumps({'username': 'testuser', 'password': 'testpassword'}),
                content_type='application/json')
    data = {"feedback": "Testing the feedback functionality"}
    client.post('/quiz/submit_feedback/', json.dumps(data), content_type='application/json')

    response = client.get('/quiz/feedback/1/')
    assert response.status_code == 200


@pytest.mark.django_db(transaction=True)
def test_get_feedback_invalid(participants):
    client.post('/quiz/login/', json.dumps({'username': 'testuser', 'password': 'testpassword'}),
                content_type='application/json')
    data = {"feedback": "Testing the feedback functionality"}
    client.post('/quiz/submit_feedback/', json.dumps(data), content_type='application/json')

    response = client.get('/quiz/feedback/11/')
    assert response.status_code == 400
    assert response.json() == {"message": "Feedback id does not exist!"}


@pytest.mark.django_db(transaction=True)
def test_get_feedback_invalid_request_method(participants):
    client.post('/quiz/login/', json.dumps({'username': 'testuser', 'password': 'testpassword'}),
                content_type='application/json')
    data = {"feedback": "Testing the feedback functionality"}
    client.post('/quiz/submit_feedback/', json.dumps(data), content_type='application/json')

    response = client.delete('/quiz/feedback/1/')
    assert response.status_code == 400
    assert response.json() == {"message": "Invalid request method"}


@pytest.mark.django_db(transaction=True)
def test_get_feedback_by_user_id(participants):
    client.post('/quiz/login/', json.dumps({'username': 'testuser', 'password': 'testpassword'}),
                content_type='application/json')
    data = {"feedback": "Testing the feedback functionality"}
    client.post('/quiz/submit_feedback/', json.dumps(data), content_type='application/json')

    response = client.get('/quiz/feedback/user/1/')
    assert response.status_code == 200


@pytest.mark.django_db(transaction=True)
def test_get_feedback_by_user_id_2(participants):
    client.post('/quiz/login/', json.dumps({'username': 'testuser', 'password': 'testpassword'}),
                content_type='application/json')
    data = {"feedback": "Testing the feedback functionality"}
    client.post('/quiz/submit_feedback/', json.dumps(data), content_type='application/json')

    response = client.get('/quiz/feedback/user/2/')
    assert response.status_code == 200
    assert response.json() == {"message": "The user did not submit any feedback !!!"}


@pytest.mark.django_db(transaction=True)
def test_get_feedback_by_user_id_invalid_user(participants):
    client.post('/quiz/login/', json.dumps({'username': 'testuser', 'password': 'testpassword'}),
                content_type='application/json')
    data = {"feedback": "Testing the feedback functionality"}
    client.post('/quiz/submit_feedback/', json.dumps(data), content_type='application/json')

    response = client.get('/quiz/feedback/user/11/')
    assert response.status_code == 400
    assert response.json() == {"message": "User does not exist!"}


@pytest.mark.django_db(transaction=True)
def test_get_feedback_user_invalid_request_method(participants):
    client.post('/quiz/login/', json.dumps({'username': 'testuser', 'password': 'testpassword'}),
                content_type='application/json')
    data = {"feedback": "Testing the feedback functionality"}
    client.post('/quiz/submit_feedback/', json.dumps(data), content_type='application/json')

    response = client.delete('/quiz/feedback/user/1/')
    assert response.status_code == 400
    assert response.json() == {"message": "Invalid request method"}
