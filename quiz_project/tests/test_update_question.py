import json

import pytest
from django.contrib.auth.models import User
from quiz_app.models.questions import Questions
from rest_framework.test import APIClient

client = APIClient()


@pytest.fixture
def admin_user():
    return User.objects.create_user(username='admin', password='admin', is_superuser=True)


@pytest.mark.django_db(transaction=True)
def test_update_questions_put_method_success(admin_user):
    client.post('/quiz/login/', json.dumps({'username': 'admin', 'password': 'admin'}),
                content_type='application/json')

    data = {
        "question": "What is capital city of Karnataka?",
        "options": ["Delhi", "Bangalore", "Hyderabad"],
        "scores": [1, 10, 1],
        "weightage": 0.25
    }

    client.post('/quiz/add_questions/', json.dumps(data), content_type='application/json')

    data = {
        "question": "What is capital city of Karnataka?",
        "options": ["Delhi", "Bangalore", "Hyderabad"],
        "scores": [2, 10, 2],
        "weightage": 0.5
    }
    response = client.put('/quiz/question/update/1/', json.dumps(data), content_type='application/json')

    assert response.status_code == 200
    assert response.json() == {"Message": "Question updated successfully .."}
    question = Questions.objects.filter(question=data['question']).first()
    assert question is not None
    assert question.question == data['question']


@pytest.mark.django_db(transaction=True)
def test_update_questions_put_method_invalid_data(admin_user):
    client.post('/quiz/login/', json.dumps({'username': 'admin', 'password': 'admin'}),
                content_type='application/json')

    data = {
        "question": "What is capital city of Karnataka?",
        "options": ["Delhi", "Bangalore", "Hyderabad"],
        "scores": [1, 10, 1],
        "weightage": 0.25
    }

    client.post('/quiz/add_questions/', json.dumps(data), content_type='application/json')

    data = {
        "questionss": "What is capital city of Karnataka?",
        "options": ["Delhi", "Bangalore", "Hyderabad"],
        "scores": [2, 10, 2],
        "weightage": 0.5
    }
    response = client.put('/quiz/question/update/1/', json.dumps(data), content_type='application/json')

    assert response.status_code == 400


@pytest.mark.django_db(transaction=True)
def test_update_questions_put_method_invalid_data2(admin_user):
    client.post('/quiz/login/', json.dumps({'username': 'admin', 'password': 'admin'}),
                content_type='application/json')

    data = {
        "question": "What is capital city of Karnataka?",
        "options": ["Delhi", "Bangalore", "Hyderabad"],
        "scores": [1, 10, 1],
        "weightage": 0.25
    }

    client.post('/quiz/add_questions/', json.dumps(data), content_type='application/json')

    data = {
        "question": "What is capital city of Karnataka?",
        "options": ["Delhi", "Bangalore", "Hyderabad"],
        "scores": [2, 10, 2, 2],
        "weightage": 0.5
    }
    response = client.put('/quiz/question/update/1/', json.dumps(data), content_type='application/json')

    assert response.status_code == 400


@pytest.mark.django_db(transaction=True)
def test_update_questions_put_method_unauthorized_user():
    data = {
        "question": "What is capital city of Karnataka?",
        "options": ["Delhi", "Bangalore", "Hyderabad"],
        "scores": [1, 10, 1],
        "weightage": 0.25
    }

    client.post('/quiz/add_questions/', json.dumps(data), content_type='application/json')

    data = {
        "question": "What is capital city of Karnataka?",
        "options": ["Delhi", "Bangalore", "Hyderabad"],
        "scores": [2, 10, 2],
        "weightage": 0.5
    }
    response = client.put('/quiz/question/update/1/', json.dumps(data), content_type='application/json')

    assert response.status_code == 400


@pytest.mark.django_db(transaction=True)
def test_update_questions_put_method_invalid_data3(admin_user):
    client.post('/quiz/login/', json.dumps({'username': 'admin', 'password': 'admin'}),
                content_type='application/json')

    data = {
        "question": "What is capital city of Karnataka?",
        "options": ["Delhi", "Bangalore", "Hyderabad"],
        "scores": [1, 10, 1],
        "weightage": 0.25
    }

    client.post('/quiz/add_questions/', json.dumps(data), content_type='application/json')

    data = {
        "question": "What is capital city of Karnataka?",
        "options": ["Delhi", "Bangalore", "Hyderabad"],
        "scores": [2, 10, 2],
        "weightage": 0.5
    }
    response = client.put('/quiz/question/update/111/', json.dumps(data), content_type='application/json')

    assert response.status_code == 400
    assert response.json() == {'Message': 'The questions does not exist'}


@pytest.mark.django_db(transaction=True)
def test_update_questions_patch_method_success(admin_user):
    client.post('/quiz/login/', json.dumps({'username': 'admin', 'password': 'admin'}),
                content_type='application/json')

    data = {
        "question": "What is capital city of Karnataka?",
        "options": ["Delhi", "Bangalore", "Hyderabad"],
        "scores": [1, 10, 1],
        "weightage": 0.25
    }

    client.post('/quiz/add_questions/', json.dumps(data), content_type='application/json')

    data = {"question": "What is capital city of Karnataka?"}
    response = client.patch('/quiz/question/update/1/', json.dumps(data), content_type='application/json')

    assert response.status_code == 200


@pytest.mark.django_db(transaction=True)
def test_update_questions_patch_method_success_1(admin_user):
    client.post('/quiz/login/', json.dumps({'username': 'admin', 'password': 'admin'}),
                content_type='application/json')

    data = {
        "question": "What is capital city of Karnataka?",
        "options": ["Delhi", "Bangalore", "Hyderabad"],
        "scores": [1, 10, 1],
        "weightage": 0.25
    }

    client.post('/quiz/add_questions/', json.dumps(data), content_type='application/json')

    data = {
        "options": ["Delhi", "Bangalore", "Hyderabdfgad"]

    }
    response = client.patch('/quiz/question/update/1/', json.dumps(data), content_type='application/json')

    # assert response.status_code == 200
    assert response.json() == {'Message': 'Question updated successfully ..'}


@pytest.mark.django_db(transaction=True)
def test_update_questions_patch_method_success_2(admin_user):
    client.post('/quiz/login/', json.dumps({'username': 'admin', 'password': 'admin'}),
                content_type='application/json')

    data = {
        "question": "What is capital city of Karnataka?",
        "options": ["Delhi", "Bangalore", "Hyderabad"],
        "scores": [1, 10, 1],
        "weightage": 0.25
    }

    client.post('/quiz/add_questions/', json.dumps(data), content_type='application/json')

    data = {
        "scores": [1, 10, 1]
    }
    response = client.patch('/quiz/question/update/1/', json.dumps(data), content_type='application/json')

    assert response.status_code == 200


@pytest.mark.django_db(transaction=True)
def test_update_questions_patch_method_success_3(admin_user):
    client.post('/quiz/login/', json.dumps({'username': 'admin', 'password': 'admin'}),
                content_type='application/json')

    data = {
        "question": "What is capital city of Karnataka?",
        "options": ["Delhi", "Bangalore", "Hyderabad"],
        "scores": [1, 10, 1],
        "weightage": 0.25
    }

    client.post('/quiz/add_questions/', json.dumps(data), content_type='application/json')

    data = {
        "weightage": 0.25
    }
    response = client.patch('/quiz/question/update/1/', json.dumps(data), content_type='application/json')

    assert response.status_code == 200


@pytest.mark.django_db(transaction=True)
def test_update_questions_patch_method_invalid_data_1(admin_user):
    client.post('/quiz/login/', json.dumps({'username': 'admin', 'password': 'admin'}),
                content_type='application/json')

    data = {
        "question": "What is capital city of Karnataka?",
        "options": ["Delhi", "Bangalore", "Hyderabad"],
        "scores": [1, 10, 1],
        "weightage": 0.25
    }

    client.post('/quiz/add_questions/', json.dumps(data), content_type='application/json')

    data = {
        "options": ["Delhi", "Bangalore", "Hyderabad", "Goa"]

    }
    response = client.patch('/quiz/question/update/1/', json.dumps(data), content_type='application/json')

    assert response.status_code == 400


@pytest.mark.django_db(transaction=True)
def test_update_questions_patch_method_invalid_data_2(admin_user):
    client.post('/quiz/login/', json.dumps({'username': 'admin', 'password': 'admin'}),
                content_type='application/json')

    data = {
        "question": "What is capital city of Karnataka?",
        "options": ["Delhi", "Bangalore", "Hyderabad"],
        "scores": [1, 10, 1],
        "weightage": 0.25
    }

    client.post('/quiz/add_questions/', json.dumps(data), content_type='application/json')

    data = {
        "scores": [1, 10],

    }
    response = client.patch('/quiz/question/update/1/', json.dumps(data), content_type='application/json')

    assert response.status_code == 400


@pytest.mark.django_db(transaction=True)
def test_update_questions_patch_method_invalid_data_3(admin_user):
    client.post('/quiz/login/', json.dumps({'username': 'admin', 'password': 'admin'}),
                content_type='application/json')

    data = {
        "question": "What is capital city of Karnataka?",
        "options": ["Delhi", "Bangalore", "Hyderabad"],
        "scores": [1, 10, 1],
        "weightage": 0.25
    }

    client.post('/quiz/add_questions/', json.dumps(data), content_type='application/json')

    data = {"daad": "Ada"}
    response = client.patch('/quiz/question/update/1/', json.dumps(data), content_type='application/json')

    assert response.status_code == 400
    assert response.json() == {'Message': 'Invalid data provided'}


@pytest.mark.django_db(transaction=True)
def test_update_questions_patch_method_invalid_data_4(admin_user):
    client.post('/quiz/login/', json.dumps({'username': 'admin', 'password': 'admin'}),
                content_type='application/json')

    data = {
        "question": "What is capital city of Karnataka?",
        "options": ["Delhi", "Bangalore", "Hyderabad"],
        "scores": [1, 10, 1],
        "weightage": 0.25
    }

    client.post('/quiz/add_questions/', json.dumps(data), content_type='application/json')

    data = {"scores": [1, 10, 1]}
    response = client.patch('/quiz/question/update/11/', json.dumps(data), content_type='application/json')

    assert response.status_code == 400


@pytest.mark.django_db(transaction=True)
def test_update_questions_patch_method_unauthorized_user():
    data = {
        "question": "What is capital city of Karnataka?",
        "options": ["Delhi", "Bangalore", "Hyderabad"],
        "scores": [1, 10, 1],
        "weightage": 0.25
    }

    client.post('/quiz/add_questions/', json.dumps(data), content_type='application/json')

    data = {
        "weightage": 0.25
    }
    response = client.patch('/quiz/question/update/1/', json.dumps(data), content_type='application/json')

    assert response.status_code == 400


@pytest.mark.django_db(transaction=True)
def test_update_questions_invalid_request_method(admin_user):
    data = {
        "question": "What is capital city of Karnataka?",
        "options": ["Delhi", "Bangalore", "Hyderabad"],
        "scores": [1, 10, 1],
        "weightage": 0.25
    }

    client.post('/quiz/add_questions/', json.dumps(data), content_type='application/json')

    response = client.get('/quiz/question/update/1/')

    assert response.status_code == 400
