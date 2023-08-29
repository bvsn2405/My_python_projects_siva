import json
from quiz_app.models.feedback import Feedback
import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient

client = APIClient()


@pytest.fixture
def participants():
    return User.objects.create_user(username='testuser', password='testpassword')


@pytest.mark.django_db(transaction=True)
def test_submit_feedback_success(participants):
    """Verifying submit feedback functionality with valid data with authorization"""
    client.post('/quiz/login/', json.dumps({'username': 'testuser', 'password': 'testpassword'}),
                content_type='application/json')

    data = {

        "feedback": "Testing the feedback functionality"
    }

    response = client.post('/quiz/submit_feedback/', json.dumps(data), content_type='application/json')

    assert response.status_code == 200


@pytest.mark.django_db(transaction=True)
def test_submit_feedback_without_authorization():
    """Verifying submit feedback functionality with valid data and without authorization"""

    data = {

        "feedback": "Testing the feedback functionality"
    }

    response = client.post('/quiz/submit_feedback/', json.dumps(data), content_type='application/json')

    assert response.status_code == 400
    assert response.json() == {"message": "User is not authenticated"}


@pytest.mark.django_db(transaction=True)
def test_submit_feedback_with_invalid_request_method(participants):

    """Verifying submit feedback functionality with valid data and with invalid request method"""

    client.post('/quiz/login/', json.dumps({'username': 'testuser', 'password': 'testpassword'}),
                content_type='application/json')
    data = {

        "feedback": "Testing the feedback functionality"
    }

    response = client.put('/quiz/submit_feedback/', json.dumps(data), content_type='application/json')

    assert response.status_code == 400
    assert response.json() == {"message": "Invalid request method"}
