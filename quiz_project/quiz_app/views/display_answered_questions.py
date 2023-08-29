import json

from django.contrib.auth.models import User
from django.db.models import Sum, Count
from django.http import JsonResponse
from quiz_app.models.answered_questions import Answered_Questions
from quiz_app.models.questions import Questions


def display_answered_questions(request):
    """
    View function to display all questions answered by the current user.

    Accepts a GET request to retrieve all questions that have been answered by the current user.
    Returns a JSON response containing details of the answered questions, including question text, options,
    scores, and the submitted answer by the user.

    Returns:
        JsonResponse: JSON response with details of the answered questions.

    Example Usage:
        - Request URL: GET /quiz/answered_questions/
        - Response:
            {
                "user": "username",
                "data": [
                    {
                        "1.question": "What is the capital of France?",
                        "options": ["London", "Paris", "Berlin"],
                        "scores": [0, 1, 0],
                        "submitted answer": "Paris"
                    },
                    {
                        "2.question": "What is the largest mammal?",
                        "options": ["Elephant", "Blue Whale", "Giraffe"],
                        "scores": [0, 1, 0],
                        "submitted answer": "Blue Whale"
                    },
                    ...
                ],
                "Attempted Questions": 10,
                "Total Score": 20
            }
    """
    if request.method == "GET":
        user = User.objects.get(username=request.user.username)
        id = user.id
        answered_questions = Answered_Questions.objects.filter(user_id=id)
        data = []
        total_score = answered_questions.aggregate(total=Sum('score'))['total']
        attempted_questions = answered_questions.aggregate(count=Count('score'))['count']

        for ans_qstn in answered_questions:
            que = Questions.objects.get(id=ans_qstn.question_id)
            question_data = {
                f'{que.id}.question': que.question,
                'options': json.loads(que.options),
                'scores': que.scores,
                'submitted answer': ans_qstn.submitted_answer,
            }
            data.append(question_data)

        return JsonResponse({"user": request.user.username, 'data': data, "Attempted Questions": attempted_questions,
                             "Total Score ": total_score})

    else:
        return JsonResponse({"message": "Invalid request method"}, status=400)

