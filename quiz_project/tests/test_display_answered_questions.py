import json

import pytest
from django.contrib.auth.models import User
from quiz_app.models.questions import Questions
from rest_framework.test import APIClient

client = APIClient()


@pytest.fixture
def participants():
    return User.objects.create_user(username='testuser', password='testpassword')


@pytest.fixture
def question():
    user = User.objects.create_user(username='testuser1', password='testpassword',is_superuser=True)
    return Questions.objects.create(
        user=user,
        question='What is the capital of France?',
        options='["Paris", "London", "Berlin"]',
        scores='[10, 1, 1]',
        weightage=5.0
    ), Questions.objects.create(
        user=user,
        question='What is the capital of England?',
        options='["Paris", "London", "Berlin"]',
        scores='[1, 10, 1]',
        weightage=5.0
    )


@pytest.mark.django_db
def test_display_answered_question_success(participants, question):

    client.post('/quiz/login/', json.dumps({'username': 'testuser', 'password': 'testpassword'}),
                content_type='application/json')
    data = {"submitted_answer": "Berlin"}
    data2 = {"submitted_answer": "London"}


    client.post('/quiz/questions/submit_answer/1/', json.dumps(data), content_type="application/json")
    client.post('/quiz/questions/submit_answer/2/', json.dumps(data2), content_type="application/json")

    response = client.get('/quiz/answered_questions/')
    assert response.status_code == 200



@pytest.mark.django_db
def test_display_answered_questions_invalid_request_method(participants, question):

    client.post('/quiz/login/', json.dumps({'username': 'testuser', 'password': 'testpassword'}),
                content_type='application/json')
    data = {"submitted_answer": "Berlin"}
    data2 = {"submitted_answer": "London"}


    client.post('/quiz/questions/submit_answer/1/', json.dumps(data), content_type="application/json")
    client.post('/quiz/questions/submit_answer/2/', json.dumps(data2), content_type="application/json")

    response = client.delete('/quiz/answered_questions/')
    assert response.status_code == 400
    assert response.json() == {"message": "Invalid request method"}


@pytest.mark.django_db
def test_display_answered_questions_with_unauthorized_user(question):

    data = {"submitted_answer": "Berlin"}
    data2 = {"submitted_answer": "London"}

    client.post('/quiz/questions/submit_answer/1/', json.dumps(data), content_type="application/json")
    client.post('/quiz/questions/submit_answer/2/', json.dumps(data2), content_type="application/json")

    response = client.delete('/quiz/answered_questions/')
    assert response.status_code == 400
    assert response.json() == {"message": "User is not authenticated"}
