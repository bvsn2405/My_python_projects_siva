from django.http import JsonResponse


class CustomAuthenticationMiddleware:
    """
    Custom middleware to handle authentication for specific URL paths.

    This middleware checks whether the user is authenticated or not for specific URL paths
    and bypasses the authentication check for those paths. For other paths, it checks if the user
    is authenticated. If the user is not authenticated, it returns a JSON response with a message
    indicating that the user is not authenticated.

    Args:
        get_response (callable): The next middleware or view function in the request-response chain.

    Returns:
        HttpResponse: The response from the view function or next middleware.

    Example Usage:
        # In settings.py, add the middleware to the MIDDLEWARE setting:
        MIDDLEWARE = [
            ...
            'quiz_app.middlewares.middleware.CustomAuthenticationMiddleware',
            ...
        ]

        # The middleware will check if the user is authenticated for specific URL paths:
        # - /quiz/participants/reg/
        # - /quiz/login/
        # - /quiz/logout/
        # - /quiz/questions/
        # - /quiz/ranks/
        # - /quiz/scores/
        # - /quiz/feedback/
        # - Any URL path starting with /quiz/question/
        # - Any URL path starting with /quiz/feedback/
        # - Any URL path starting with /quiz/participants/update/
        # For these paths, the middleware will continue the request-response chain.
        # For other paths, if the user is not authenticated, it will return a JSON response
        # with the message "User is not authenticated".
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        paths = [
            "/quiz/participants/reg/",
            "/quiz/login/",
            "/quiz/logout/",
            "/quiz/questions/",
            "/quiz/ranks/",
            "/quiz/scores/",
            "/quiz/feedback/",
            "/quiz/forgot_password/",
            "/quiz/forgot_password/otp_validation"
        ]

        if request.path in paths or request.path.startswith("/quiz/question/") or \
                request.path.startswith("/quiz/feedback/") :
            response = self.get_response(request)
            return response
        else:
            if not request.user.is_authenticated:
                return JsonResponse({"message": "User is not authenticated"},status=400)

            response = self.get_response(request)
        return response
