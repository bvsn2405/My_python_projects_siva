import json
import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from quiz_app.models.questions import Questions

client = APIClient()


@pytest.fixture
def admin_user():
    return User.objects.create_user(username='admin', password='admin', is_superuser=True)


@pytest.fixture
def participants():
    return User.objects.create_user(username='testuser', password='testpassword')


@pytest.mark.django_db(transaction=True)
def test_add_questions_success(admin_user):
    """Verifying add questions functionality with valid data with admin"""
    client.post('/quiz/login/', json.dumps({'username': 'admin', 'password': 'admin'}),
                content_type='application/json')

    data = {
        "question": "What is capital city of Karnataka?",
        "options": ["Delhi", "Bangalore", "Hyderabad"],
        "scores": [1, 10, 1],
        "weightage": 0.25
    }

    response = client.post('/quiz/add_questions/', json.dumps(data), content_type='application/json')

    assert response.status_code == 200
    assert response.json() == {
        "message": "Question added successfully",
        "question": "What is capital city of Karnataka?",
        "Question Weightage": 0.25,
        "options,scores": {
            "Delhi": 1,
            "Bangalore": 10,
            "Hyderabad": 1
        }
    }
    question = Questions.objects.filter(question=data['question']).first()
    assert question is not None
    assert question.question == data['question']


@pytest.mark.django_db
def test_add_questions_unauthorized_user(participants):
    """Verifying add questions functionality with valid data with unauthorized user"""
    client.post('/quiz/login/', json.dumps({'username': 'testuser', 'password': 'testpassword'}),
                content_type='application/json')

    data = {
        "question": "What is capital city of Karnataka?",
        "options": ["Delhi", "Bangalore", "Hyderabad"],
        "scores": [1, 10, 1],
        "weightage": 0.25
    }

    response = client.post('/quiz/add_questions/', json.dumps(data), content_type='application/json')

    assert response.status_code == 400
    assert response.json() == {"message": "Sorry, You don't have permissions to add a Question"}


@pytest.mark.django_db
def test_add_questions_with_invalid1(admin_user):
    """Verifying add questions functionality with invalid data by sending empty payload"""
    client.post('/quiz/login/', json.dumps({'username': 'admin', 'password': 'admin'}),
                content_type='application/json')

    data = {
    }

    response = client.post('/quiz/add_questions/', json.dumps(data), content_type='application/json')

    assert response.status_code == 400
    assert response.json() == {
        "Error Message": "Invalid data"
    }


@pytest.mark.django_db
def test_add_questions_with_invalid_data2(admin_user):
    """Verifying add questions functionality with invalid data by providing more options in options filed and
    fewer scores in scores filed"""
    client.post('/quiz/login/', json.dumps({'username': 'admin', 'password': 'admin'}),
                content_type='application/json')

    data = {
        "question": "What is capital city of Karnataka?",
        "options": ["Delhi", "Bangalore", "Hyderabad", 'Goa'],
        "scores": [1, 10, 1],
        "weightage": 0.25
    }

    response = client.post('/quiz/add_questions/', json.dumps(data), content_type='application/json')

    assert response.status_code == 400
    assert response.json() == {
        "Error Message": "You should assign only one score to each option."
    }
