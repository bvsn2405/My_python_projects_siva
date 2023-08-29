import json

from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from quiz_app.models.questions import Questions


@csrf_exempt
def display_all_questions(request):
    """
    View function to display all non-deleted questions in the database.

    Accepts a GET request to retrieve all questions that are not marked as deleted.
    Returns a JSON response containing a list of question details, including question text,
        weightage, options, and scores.

    Returns:
        JsonResponse: JSON response with a list of non-deleted question details.

    Example Usage:
        - Request URL: GET /quiz/questions/
        - Response:
         If the user is superuser:
            [
                {
                    "1.question": "What is the capital of France?",
                    "Question Weightage": 5,
                    "options": ["London", "Paris", "Berlin"],
                    "scores": [0, 1, 0]

                },
                {
                    "2.question": "What is the largest mammal?",
                    "Question Weightage": 3,
                    "options": ["Elephant", "Blue Whale", "Giraffe"],
                    "scores": [0, 1, 0]
                },
                ...
            ]

         If the user is not superuser :
          [
                {
                    "1.question": "What is the capital of France?",
                    "Question Weightage": 5,
                    "options": ["London", "Paris", "Berlin"]
                },
                {
                    "2.question": "What is the largest mammal?",
                    "Question Weightage": 3,
                    "options": ["Elephant", "Blue Whale", "Giraffe"]
                },
                ...
            ]
    """

    if request.method == "GET":

        questions = Questions.objects.filter(is_deleted=False)
        question_list = []
        try:
            user = User.objects.get(username=request.user.username)
            if user.is_superuser is True:
                for question in questions:
                    question_data = {
                        f'{question.id}.question': question.question,
                        'Question Weightage': question.weightage,
                        'options': json.loads(question.options),
                        'scores': json.loads(question.scores)}
                    question_list.append(question_data)
                return JsonResponse(question_list, safe=False)

        except:

            for question in questions:
                question_data = {
                    f'{question.id}.question': question.question,
                    'Question Weightage': question.weightage,
                    'options': json.loads(question.options)}
                question_list.append(question_data)
            return JsonResponse(question_list, safe=False)
    else:

        return JsonResponse({"message": "Invalid request method"}, status=400)

@csrf_exempt
def display_question(request, id):
    """
    View function to display a specific question.

    Accepts a GET request to fetch and display the question with the provided ID.
    Retrieves the question data from the 'Questions' model based on the provided ID.
    If the question with the given ID exists and is not deleted, the function returns the question data.
    If the question does not exist or is deleted, the function returns an appropriate error message.
    Returns a JSON response containing the question data or an error message.

    Args:
        request (HttpRequest): The HTTP request object.
        id (int): The ID of the question to be displayed.

    Returns:
        JsonResponse: JSON response containing the question data or an error message.

    Example Usage:
        - GET Request URL: /questions/1/ (where '1' is the ID of the question)
        - Response (Successful):
        If the user is super user:
            {
                "1.question": "Sample Question Text",
                "Question Weightage": 5,
                "options": ["Option A", "Option B", "Option C"],
                "scores": [1, 2, 3]
            }
        If the user is not super user :
            {
                "1.question": "Sample Question Text",
                "Question Weightage": 5,
                "options": ["Option A", "Option B", "Option C"],
            }
        - Response (Question Does Not Exist):
            {
                "message": "Question does not exist!"
            }
        - Response (Invalid Request Method):
            {
                "message": "Invalid request"
            }
    """
    if request.method == "GET":
        try:
            question = Questions.objects.get(id=id, is_deleted=False)
            question_data = {
                "question": question.question,
                "Question Weightage": question.weightage,
                "options": json.loads(question.options)}
            return JsonResponse(question_data)
        except Questions.DoesNotExist:
            return JsonResponse({"message": "Question does not exist!"}, status=400)
    else:
        return JsonResponse({"message": "Invalid request method"}, status=400)
