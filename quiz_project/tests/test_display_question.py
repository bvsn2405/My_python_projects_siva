import pytest
from quiz_app.models.questions import Questions
from rest_framework.test import APIClient
from django.contrib.auth.models import User
import json


client = APIClient()


@pytest.mark.django_db(transaction=True)
def test_display_question():

    """Verifying display question functionality """
    user = User.objects.create_user(username='admin', password='admin', is_superuser=True)
    Questions.objects.create(
        question="What is capital city of Karnataka?",
        options=json.dumps(["Delhi", "Bangalore", "Hyderabad"]),
        scores=json.dumps([1, 10, 1]),
        user=user,
        weightage=0.25)
    response = client.get('/quiz/question/1/')
    # assert response.status_code == 200
    assert response.json() == {
        "question": "What is capital city of Karnataka?",
        "Question Weightage": 0.25,
        "options": [
            "Delhi",
            "Bangalore",
            "Hyderabad"
        ]
    }


@pytest.mark.django_db(transaction=True)
def test_display_question_with_not_existing_question():

    """Verifying display question functionality with question which is not in database"""
    response = client.get('/quiz/question/33/')
    assert response.status_code == 400
    assert response.json() == {"message": "Question does not exist!"}


@pytest.mark.django_db(transaction=True)
def test_display_question_with_invalid_request_method():
    """Verifying display question functionality with invalid request method"""
    response = client.post('/quiz/question/1/',json.dumps({'username': 'admin', 'password': 'admin'}), content_type='application/json')
    assert response.status_code == 400
    assert response.json() == {
        "message": "Invalid request method"
    }


