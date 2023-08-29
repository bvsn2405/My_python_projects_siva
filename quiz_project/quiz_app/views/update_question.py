import json
from datetime import datetime

from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from quiz_app.models.questions import Questions


@csrf_exempt
def update_question(request, id):
    """
    View function to update a question.

    Accepts PUT and PATCH requests to update the question with the provided ID.
    If the user is a superuser, the function allows updating the question's data.
    For PUT requests, the function updates the entire question's data, including question, options, scores,
    - and weightage.
    For PATCH requests, the function allows updating specific fields of the question, such as question, options,
    - scores, or weightage.
    The function validates the data and ensures that each option has only one corresponding score.
    Returns a JSON response indicating the status of the question update.

    Args:
        request (HttpRequest): The HTTP request object.
        id (int): The ID of the question to be updated.

    Returns:
        JsonResponse: JSON response with a message indicating the status of the question update.

    Example Usage:
        - PUT Request URL: /question/update/1/ (where '1' is the ID of the question)
        - PUT Request Body:
            {
                "question": "Updated question text",
                "options": ["Option A", "Option B", "Option C"],
                "scores": [1, 2, 3],
                "weightage": 5
            }
        - PATCH Request URL: /question/update/1/ (where '1' is the ID of the question)
        - PATCH Request Body:
            {
                "question": "Updated question text"
            }
        - Response (Successful Update):
            {
                "Message": "Question updated successfully"
            }
        - Response (Invalid Update - Options and Scores Length Mismatch):
            {
                "Message": "You should assign only one score to each option."
            }
        - Response (Question Does Not Exist):
            {
                "Message": "The question does not exist"
            }
        - Response (No Permission):
            {
                "Message": "You don't have permission to update the question"
            }
        - Response (Invalid Request Method):
            {
                "Message": "Invalid Request"
            }
    """
    if request.method == "PUT":
        try:
            user = User.objects.get(username=request.user.username)
            if user.is_superuser:

                try:
                    question = Questions.objects.get(id=id)
                    data = json.loads(request.body)

                    try:

                        if len(data['options']) != len(data['scores']):
                            return JsonResponse({"Message": "You should assign only one score to each option."},
                                                status=400)
                        else:
                            question.question = data['question']
                            question.options = json.dumps(data['options'])
                            question.scores = json.dumps(data['scores'])
                            question.weightage = data['weightage']
                            question.updated_by = request.user
                            question.updated_on = datetime.now()
                            question.save()
                            return JsonResponse({"Message": "Question updated successfully .."})
                    except:
                        return JsonResponse({"Message": "Invalid Data provided"}, status=400)
                except:
                    return JsonResponse({"Message": "The questions does not exist"}, status=400)
        except:
            return JsonResponse({"Message": "You dont have permission to update the questions"}, status=400)

    if request.method == "PATCH":
        try:
            user = User.objects.get(username=request.user.username)

            if user.is_superuser:

                try:
                    Questions.objects.get(id=id)

                    data = json.loads(request.body)

                    question = Questions.objects.get(id=id)

                    if 'question' in data:
                        question.question = data['question']

                    if 'weightage' in data:
                        question.weightage = data['weightage']
                    if 'options' in data and 'scores' in data:
                        if len(data['options']) == len(data['scores']):
                            question.options = json.dumps(data['options'])
                            question.scores = json.dumps(data['scores'])
                        else:
                            return JsonResponse(
                                {"Message": "You should assign only one score to each option."},
                                status=400)
                    if 'scores' in data:
                        if len(data['scores']) == len(json.loads(question.options)):
                            question.scores = json.dumps(data['scores'])
                        else:
                            return JsonResponse(
                                {"Message": "You should assign only one score to each option.",
                                 "Error": "Scores are not matching to options in the database"},
                                status=400)
                    if 'options' in data:
                        if len(data['options']) == len(json.loads(question.scores)):
                            question.options = json.dumps(data['options'])
                        else:
                            return JsonResponse(
                                {"Message": "You should assign only one score to each option.",
                                 "Error": "options are not matching to scores in the database"},
                                status=400)
                    valid_keys = {'question', 'weightage', 'options', 'scores'}
                    extra_keys = set(data.keys()) - valid_keys
                    if extra_keys:
                        return JsonResponse(
                            {"Message": "Invalid data provided"},status=400)

                    question.updated_by = request.user
                    question.updated_on = datetime.now()
                    question.save()
                    return JsonResponse({"Message": "Question updated successfully .."})

                except:
                    return JsonResponse({"Message": "The questions does not exist"}, status=400)
            else:
                return JsonResponse({"Message": "You dont have permission to update the questions"}, status=400)
        except:
            return JsonResponse({"Message": "User is not authenticated"}, status=400)

    else:
        return JsonResponse({"Message": "Invalid Request method"}, status=400)
