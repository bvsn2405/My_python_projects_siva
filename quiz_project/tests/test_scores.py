import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from quiz_app.models.questions import Questions
from quiz_app.models.answered_questions import Answered_Questions

client = APIClient()


@pytest.mark.django_db(transaction=True)
def test_scores():
    """Verifying scores functionality with all valid data"""
    user1 = User.objects.create(username='test_user1')
    user2 = User.objects.create(username='test_user2')
    user3 = User.objects.create(username='test_user3')
    question = Questions.objects.create(
        user=User.objects.create(username='test_user'),
        question='What is the capital of France?',
        options='["Paris", "London", "Berlin"]',
        scores='[10, 15, 9]',
        weightage=1.0
    )
    Answered_Questions.objects.create(user=user1, question=question, submitted_answer='Paris', score=10)
    Answered_Questions.objects.create(user=user2, question=question, submitted_answer='London', score=15)
    Answered_Questions.objects.create(user=user3, question=question, submitted_answer='Berlin', score=9)

    response = client.get('/quiz/scores/')

    assert response.status_code == 200
    assert response.json() == {
        "Scores Data": [
            {
                "User": "test_user1",
                "Total Score": 10,
                "Attempted Questions": 1
            },
            {
                "User": "test_user2",
                "Total Score": 15,
                "Attempted Questions": 1
            },
            {
                "User": "test_user3",
                "Total Score": 9,
                "Attempted Questions": 1
            }
        ]
    }
