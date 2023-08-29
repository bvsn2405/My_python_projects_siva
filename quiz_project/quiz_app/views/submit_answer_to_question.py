import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from quiz_app.models.answered_questions import Answered_Questions
from quiz_app.models.questions import Questions


@csrf_exempt
def submit_answer_to_question(request, id):
    """
    View function to submit an answer to a question.

    Accepts a POST request to submit an answer to the question with the provided ID.
    Checks if the question with the given ID exists and is not deleted.
    Verifies if the user has not already attempted the question.
    Validates the submitted answer against the options of the question.
    Calculates the score for the submitted answer based on the weightage and scores of the question options.
    Creates an 'Answered_Questions' entry for the user with the submitted answer and the calculated score.
    Returns a JSON response indicating the status of the answer submission.

    Args:
        request (HttpRequest): The HTTP request object.
        id (int): The ID of the question to which the answer is being submitted.

    Returns:
        JsonResponse: JSON response with a message indicating the status of the answer submission.

    Example Usage:
        - Request URL: POST /questions/submit_answer/1/ (where '1' is the ID of the question)
        - Request Body:
            {
                "submitted_answer": "Option A"
            }
        - Response (Successful Submission):
            {
                "message": "Your Answer submitted"
            }
        - Response (Invalid Submission - Answer not in Options):
            {
                "message": "You are trying to submit an answer which is not in the options"
            }
        - Response (Already Attempted):
            {
                "message": "You have already attempted the question !!!"
            }
        - Response (Question Does Not Exist):
            {
                "message": "Question does not exist"
            }
    """

    if request.method == "POST":
        data = json.loads(request.body)

        try:
            question = Questions.objects.get(id=id, is_deleted=False)

            if not Answered_Questions.objects.filter(question_id=question.id, user_id=request.user).exists():
                jsonDec = json.decoder.JSONDecoder()
                options = jsonDec.decode(question.options)
                scores = jsonDec.decode(question.scores)
                try:
                    submitted_answer = data['submitted_answer']
                    if submitted_answer in options:
                        index = options.index(submitted_answer)
                        print(index)
                        scored = scores[index]
                        Answered_Questions.objects.create(
                            user=request.user,
                            question=question,
                            submitted_answer=data['submitted_answer'],
                            score=question.weightage * scored)
                        return JsonResponse({"message": "Your Answer submitted"})
                    else:
                        return JsonResponse({"message": "Your are try to submit the answer which is not in the options"},status=400)
                except:
                    return JsonResponse({"Error message":"Invalid data"},status=400)

            else:
                return JsonResponse({"message": "Your are already attempted the question !!!"},status=400)

        except:
            return JsonResponse({"message": "Question does not exist"},status=400)

    return JsonResponse({"message": "Invalid request"},status=400)
