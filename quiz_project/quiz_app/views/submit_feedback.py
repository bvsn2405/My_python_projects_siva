import json
from datetime import datetime
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from quiz_app.models.feedback import Feedback


@csrf_exempt
def submit_feedback(request):
    """
    View function to submit feedback.

    Accepts a POST request to submit feedback from the authenticated user.
    Creates a 'Feedback' entry in the database with the submitted feedback and related details.
    Returns a JSON response confirming the successful submission of the feedback.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        JsonResponse: JSON response with a message confirming the successful submission of the feedback.

    Example Usage:
        - Request URL: POST /submit_feedback/
        - Request Body:
            {
                "feedback": "Your feedback message goes here"
            }
        - Response:
            {
                "message": "Feedback submitted successfully",
                "Feedback": "Your feedback message goes here",
                "Submitted on": "2023-07-21T15:30:00.123456Z",
                "Submitted by": "john_doe"
            }
    """
    try:
        if request.method == "POST":

            data = json.loads(request.body)

            Feedback.objects.create(
                user=request.user,
                feedback=data['feedback'],
                created_on=datetime.now(),
                created_by=request.user
            )
            feedback_data = {
                'message': "Feedback submitted successfully",
                'Feedback': data['feedback'],
                'Submitted on': datetime.now(),
                'Submitted by': request.user.username,
            }

            return JsonResponse(feedback_data)
    except:
        return JsonResponse({"message": "Invalid request method"},status=400)

    return JsonResponse({"message": "Invalid request method"}, status=400)

