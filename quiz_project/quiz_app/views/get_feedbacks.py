from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from quiz_app.models.feedback import Feedback


@csrf_exempt
def get_feedbacks(request):
    """
    View function to retrieve all feedbacks in the system.

    Accepts a GET request to retrieve all feedbacks stored in the database.
    Returns a JSON response containing a list of all feedback entries.

    Returns:
        JsonResponse: JSON response with a list of all feedback entries.

    Example Usage:
        - Request URL: GET /quiz/feedbacks/
        - Response:
            [
                {
                    "id": 1,
                    "user_id": 1,
                    "feedback_text": "This is a great app!",
                    "created_on": "2023-07-21T12:34:56Z"
                },
                {
                    "id": 2,
                    "user_id": 2,
                    "feedback_text": "Thank you for this wonderful quiz.",
                    "created_on": "2023-07-22T09:45:32Z"
                },
                ...
            ]
    """
    # try:
    if request.method == "GET":
        feedbacks = Feedback.objects.all().values()
        feedbacks_list = []
        for feedback in feedbacks:
            feedbacks_list.append(feedback)
        return JsonResponse(feedbacks_list, safe=False)
    else:
        return JsonResponse({"message": "Invalid request method"}, status=400)


@csrf_exempt
def get_feedback_by_id(request, id):
    """
    View function to retrieve feedback by its ID.

    Accepts a GET request with the 'id' parameter to retrieve feedback with the given ID.
    Returns a JSON response containing the details of the feedback with the provided ID.

    Args:
        request (HttpRequest): The HTTP request object.
        id (int): The ID of the feedback to be retrieved.

    Returns:
        JsonResponse: JSON response with the details of the feedback with the provided ID.

    Example Usage:
        - Request URL: GET /quiz/feedback/1/ (where '1' is the ID of the feedback to be retrieved)
        - Response:
            {
                "Feedback": [
                    {
                        "id": 1,
                        "user_id": 1,
                        "feedback_text": "This is a great app!",
                        "created_on": "2023-07-21T12:34:56Z"
                    }
                ]
            }
    """

    if request.method == "GET":
        try:
            feedback = Feedback.objects.get(id=id)
            user = User.objects.get(id=feedback.created_by_id)
            feedback_data = {
                "Feedback": feedback.feedback,
                "Posted By": user.username,
                "Posted on": feedback.created_on}
            return JsonResponse({"Feedback": feedback_data})
        except:
            return JsonResponse({"message": "Feedback id does not exist!"}, status=400)
    else:
        return JsonResponse({"message": "Invalid request method"}, status=400)


@csrf_exempt
def get_feedback_by_user_id(request, user_id):
    """
    View function to retrieve feedback submitted by a specific user.

    Accepts a GET request with the 'user_id' parameter to retrieve feedback submitted by the user with the
    - given user ID.
    Returns a JSON response containing a list of all feedback entries submitted by the user.

    Args:
        request (HttpRequest): The HTTP request object.
        user_id (int): The ID of the user whose feedback is to be retrieved.

    Returns:
        JsonResponse: JSON response with a list of feedback entries submitted by the user.

    Example Usage:
        - Request URL: GET /quiz/feedback/user/1/ (where '1' is the ID of the user)
        - Response:
            {
                "Feedback": [
                    {
                        "id": 1,
                        "user_id": 1,
                        "feedback_text": "This is a feedback!",
                        "created_on": "2023-07-21T12:34:56Z"
                    },
                    {
                        "id": 3,
                        "user_id": 1,
                        "feedback_text": "The quiz was fun!",
                        "created_on": "2023-07-25T17:22:10Z"
                    },
                    ...
                ]
            }
    """

    if request.method == "GET":

        try:
            User.objects.get(id=user_id)

            if Feedback.objects.filter(user_id=user_id).exists():
                feedback = Feedback.objects.filter(user_id=user_id).values()
                return JsonResponse({"Feedback": list(feedback)})
            else:
                return JsonResponse({"message": "The user did not submit any feedback !!!"}, status=200)

        except User.DoesNotExist:
            return JsonResponse({"message": "User does not exist!"}, status=400)
    else:
        return JsonResponse({"message": "Invalid request method"}, status=400)

