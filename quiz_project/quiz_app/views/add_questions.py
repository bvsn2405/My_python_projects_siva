import json
from datetime import datetime

from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from quiz_app.models.questions import Questions
from quiz_app.utilities.validations import verify_OptionsScores


@csrf_exempt
def add_questions(request):
    """
    View function for adding a new question to the database.

    Accepts a POST request with JSON data containing the details of the question.
    The user must be a superuser to add a question.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        JsonResponse: JSON response with information about the result of the question addition.
        If the question is added successfully, the response contains the details of the added question.
        If there is an error, the response contains an error message.

    JSON Data Format:
        {
            "question": "The question text",
            "options": ["Option 1", "Option 2", ...],
            "scores": [score_for_option_1, score_for_option_2, ...],
            "weightage": question_weightage
        }

    Note:
        - The 'options' and 'scores' arrays should have the same length.
        - The 'weightage' field represents the weightage of the question.

    Example Usage:
        - Request URL: POST /quiz/add_questions/
        - Request Body:
            {
                "question": "What is the capital of France?",
                "options": ["London", "Paris", "Berlin"],
                "scores": [0, 1, 0],
                "weightage": 5
            }

    """

    if request.method == "POST":
        user = User.objects.get(username=request.user.username)

        if user.is_superuser:
            try :
                data = json.loads(request.body)
                options = json.dumps(data['options'])
                scores = json.dumps(data['scores'])

                if verify_OptionsScores(data['options'], data['scores']) is True:
                    Questions.objects.create(
                        user=request.user,
                        question=data['question'],
                        options=options,
                        scores=scores,
                        weightage=data['weightage'],
                        created_on=datetime.now(),
                        created_by=request.user
                    )
                    question_data = {
                        'message': "Question added successfully",
                        'question': data['question'],
                        'Question Weightage': data['weightage'],
                        'options,scores': dict(zip(data['options'], data['scores']))
                    }

                    return JsonResponse(question_data)
                else:
                    return JsonResponse({"Error Message": verify_OptionsScores(data['options'], data['scores'])},status=400)
            except TypeError as error:
                return JsonResponse({"Error Message": f"Invalid JSON data: {str(error)}"}, status=400)
            except KeyError as error:
                return JsonResponse({"Error Message": "Invalid data"}, status=400)
        else:
            return JsonResponse({"message": "Sorry, You don't have permissions to add a Question"},status=400)
    return JsonResponse({"message": "Invalid request"})
