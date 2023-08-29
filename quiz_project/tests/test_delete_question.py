import json

import pytest
from django.contrib.auth.models import User
from quiz_app.models.questions import Questions
from rest_framework.test import APIClient

client = APIClient()


@pytest.fixture
def admin_user():
    return User.objects.create_user(username='admin', password='admin', is_superuser=True)


@pytest.fixture
def create_question(admin_user):
    user = User.objects.get(username='admin')
    return Questions.objects.create(
        question="What is capital city of Karnataka?",
        options=json.dumps(["Delhi", "Bangalore", "Hyderabad"]),
        scores=json.dumps([1, 10, 1]),
        user=user,
        weightage=0.25)


@pytest.mark.django_db(transaction=True)
def test_delete_question_success(create_question):
    client.post('/quiz/login/', json.dumps({'username': 'admin', 'password': 'admin'}), content_type='application/json')
    response = client.delete('/quiz/question/delete/1/')

    assert response.status_code == 200
    assert response.json() == {"Message": "Question deleted successfully .."}


@pytest.mark.django_db(transaction=True)
def test_delete_question_not_in_database(create_question):
    client.post('/quiz/login/', json.dumps({'username': 'admin', 'password': 'admin'}), content_type='application/json')
    response = client.delete('/quiz/question/delete/22/')

    assert response.status_code == 400
    assert response.json() == {"Message": "The questions does not exist"}


@pytest.mark.django_db(transaction=True)
def test_delete_question_with_unauthorized_user(create_question):
    response = client.delete('/quiz/question/delete/22/')

    assert response.status_code == 400
    assert response.json() == {"Message": "You dont have permission to update the questions"}


@pytest.mark.django_db(transaction=True)
def test_delete_question_with_invalid_request_method(create_question):
    response = client.get('/quiz/question/delete/1/')

    assert response.status_code == 400
    assert response.json() == {"Message": "Invalid Request method"}

