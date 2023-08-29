import json
import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from quiz_app.models.questions import Questions

client = APIClient()


@pytest.fixture
def participants():
    return User.objects.create_user(username='testuser', password='testpassword')


@pytest.fixture
def question():
    Questions.objects.create(
        user=User.objects.create(username='test_user'),
        question='What is the capital of France?',
        options='["Paris", "London", "Berlin"]',
        scores='[10, 0, 0]',
        weightage=5.0
    )


@pytest.mark.django_db
def test_submit_answer_to_a_question(participants, question):
    """Verifying submit answer to question functionality with all valid data and authorized user"""

    client.post('/quiz/login/', json.dumps({'username': 'testuser', 'password': 'testpassword'}),
                content_type='application/json')
    data = {

        "submitted_answer": "Berlin"

    }

    request = client.post('/quiz/questions/submit_answer/1/', json.dumps(data), content_type="application/json")
    assert request.status_code == 200
    assert request.json() == {"message": "Your Answer submitted"}


@pytest.mark.django_db
def test_submit_answer_to_a_question_with_invalid_data(participants, question):
    """Verifying submit answer to question functionality with invalid data and authorized user"""

    client.post('/quiz/login/', json.dumps({'username': 'testuser', 'password': 'testpassword'}),
                content_type='application/json')
    data = {

        "submitted_answer": "Delhi"

    }

    request = client.post('/quiz/questions/submit_answer/1/', json.dumps(data), content_type="application/json")
    assert request.status_code == 400
    assert request.json() == {"message": "Your are try to submit the answer which is not in the options"}


@pytest.mark.django_db
def test_submit_answer_to_a_question_with_invalid_data2(participants, question):
    """Verifying submit answer to question functionality with invalid data by keeping 'submitted_answer' field
     empty and authorized user"""

    client.post('/quiz/login/', json.dumps({'username': 'testuser', 'password': 'testpassword'}),
                content_type='application/json')
    data = {}

    request = client.post('/quiz/questions/submit_answer/1/', json.dumps(data), content_type="application/json")
    assert request.status_code == 400
    assert request.json() == {"Error message": "Invalid data"}


@pytest.mark.django_db
def test_submit_answer_to_a_question_with_invalid_data3(participants):
    """Verifying submit answer to question functionality with invalid data answering a question
     which is not in database and authorized user"""

    client.post('/quiz/login/', json.dumps({'username': 'testuser', 'password': 'testpassword'}),
                content_type='application/json')
    data = {

        "submitted_answer": "Delhi"

    }

    request = client.post('/quiz/questions/submit_answer/7/', json.dumps(data), content_type="application/json")
    assert request.status_code == 400
    assert request.json() == {"message": "Question does not exist"}


@pytest.mark.django_db
def test_submit_answer_to_a_question_already_answered(participants, question):
    """Verifying submit answer to question functionality by answering again with authorized user"""

    client.post('/quiz/login/', json.dumps({'username': 'testuser', 'password': 'testpassword'}),
                content_type='application/json')
    data = {

        "submitted_answer": "Paris"

    }

    client.post('/quiz/questions/submit_answer/1/', json.dumps(data), content_type="application/json")

    request = client.post('/quiz/questions/submit_answer/1/', json.dumps(data), content_type="application/json")

    assert request.status_code == 400
    assert request.json() == {"message": "Your are already attempted the question !!!"}


@pytest.mark.django_db
def test_submit_answer_to_a_question_without_authorizing():
    """Verifying submit answer to question functionality with all valid data and unauthorized user"""

    data = {"submitted_answer": "Berlin"}

    request = client.post('/quiz/questions/submit_answer/1/', json.dumps(data), content_type="application/json")
    assert request.status_code == 400
    assert request.json() == {
        "message": "User is not authenticated"
    }
