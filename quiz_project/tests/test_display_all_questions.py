import json

import pytest
from django.contrib.auth.models import User
from quiz_app.models.questions import Questions
from rest_framework.test import APIClient

client = APIClient()


@pytest.fixture()
def super_user():
    return User.objects.create_user(username='admin', password='admin', is_superuser=True)


@pytest.fixture
def question():
    user = User.objects.create_user(username='testuser1', password='testpassword', is_superuser=True)
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


@pytest.mark.django_db(transaction=True)
def test_display_all_questions_without_authorize(question):
    """Verifying display all questions functionality without authorizing"""
    response = client.get('/quiz/questions/')
    assert response.status_code == 200
    assert response.json() == [{'1.question': 'What is the capital of France?', 'Question Weightage': 5.0,
                                'options': ['Paris', 'London', 'Berlin']},
                               {'2.question': 'What is the capital of England?',
                                'Question Weightage': 5.0,
                                'options': ['Paris', 'London', 'Berlin']}]


@pytest.mark.django_db(transaction=True)
def test_display_all_questions_with_authorize():
    """Verifying display all questions functionality with authorizing"""
    User.objects.create_user(username='admin', password='admin', is_superuser=True)

    client.post('/quiz/login/', json.dumps({'username': 'admin', 'password': 'admin'}), content_type='application/json')
    response = client.get('/quiz/questions/')
    assert response.status_code == 200


@pytest.mark.django_db(transaction=True)
def test_display_all_questions_with_invalid_request_method():
    """Verifying display all questions functionality with invalid request method"""
    response = client.post('/quiz/questions/', json.dumps({'username': 'admin', 'password': 'admin'}),
                           content_type='application/json')
    assert response.status_code == 400
    assert response.json() == {
        "message": "Invalid request method"
    }


@pytest.mark.django_db(transaction=True)
def test_display_one_question_with_invalid_request_method():
    """Verifying display all questions functionality with invalid request method"""
    response = client.post('/quiz/question/1/', json.dumps({'username': 'admin', 'password': 'admin'}),
                           content_type='application/json')
    assert response.status_code == 400
    assert response.json() == {
        "message": "Invalid request method"
    }


@pytest.mark.django_db(transaction=True)
def test_display_one_question(question):
    response = client.get('/quiz/question/1/')
    assert response.status_code == 200


@pytest.mark.django_db(transaction=True)
def test_display_one_question_not_in_database(question):
    response = client.get('/quiz/question/11/')
    assert response.status_code == 400
