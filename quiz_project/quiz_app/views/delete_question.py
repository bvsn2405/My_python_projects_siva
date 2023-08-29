from datetime import datetime

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from quiz_app.models.questions import Questions


@csrf_exempt
def delete_question(request, id):
    """
    View function to delete a question from the database.

    Accepts a DELETE request to delete a question with the given 'id'.
    The user must be a superuser to delete a question.

    Args:
        request (HttpRequest): The HTTP request object.
        id (int): The ID of the question to be deleted.

    Returns:
        JsonResponse: JSON response with information about the result of the question deletion.
        If the question is deleted successfully, the response contains a success message.
        If the question does not exist or if the user doesn't have permission, an appropriate message is returned.

    Example Usage:
        - Request URL: DELETE /quiz/question/delete/1/ (where '1' is the ID of the question to be deleted)

    """
    if request.method == "DELETE":
        user = request.user
        if user.is_superuser:
            try:
                question = Questions.objects.get(id=id)
                question.deleted_by = request.user
                question.deleted_on = datetime.now()
                question.is_deleted = True
                question.save()
                return JsonResponse({"Message": "Question deleted successfully .."})

            except:
                return JsonResponse({"Message": "The questions does not exist"}, status=400)
        else:
            return JsonResponse({"Message": "You dont have permission to update the questions"}, status=400)

    else:
        return JsonResponse({"Message": "Invalid Request method"}, status=400)
