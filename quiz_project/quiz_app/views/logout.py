from django.contrib.auth import logout
from django.http import JsonResponse


def logout_view(request):
    """
    View function to log out the currently authenticated user.

    Checks if the user is authenticated (logged in).
    If the user is logged in, logs them out using Django's `logout` method and returns a success message.
    If the user is not logged in, returns a message indicating that the user is already logged out.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        JsonResponse: JSON response with a message indicating the status of the logout attempt.

    Example Usage:
        - Request URL: GET /logout/
        - Response (User Logged In):
            {
                "message": "Logged out successfully"
            }
        - Response (User Not Logged In):
            {
                "message": "Already logged out"
            }
    """
    if request.user.is_authenticated:
        logout(request)
        return JsonResponse({'message': 'Logged out successfully'})
    else:
        return JsonResponse({'message': 'Already logged out'}, status=400)
