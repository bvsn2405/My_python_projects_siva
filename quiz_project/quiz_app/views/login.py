import json

from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def login_view(request):
    """
    View function to authenticate and log in a user.

    Accepts a POST request with user credentials (username and password) in JSON format.
    Attempts to authenticate the user with the provided credentials.
    If authentication is successful, logs in the user and returns a success message.
    If authentication fails, returns an error message with HTTP status code 401.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        JsonResponse: JSON response with a message indicating the status of the login attempt.

    Example Usage:
        - Request URL: POST /login/
        - Request Body: {"username": "john_doe", "password": "password123"}
        - Response (Success):
            {
                "message": "successfully logged in"
            }
        - Response (Failure):
            {
                "message": "Invalid credentials"
            }
    """
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            username = data['username']
            password = data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)

                return JsonResponse({'message': "successfully logged in"})
            else:
                return JsonResponse({'message': 'Invalid credentials'}, status=400)
        except:
            return JsonResponse({'message': 'Invalid data'}, status=400)
    else:
        return JsonResponse({'message': 'Invalid request method'}, status=400)
