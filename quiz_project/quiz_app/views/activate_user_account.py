from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator


def activate_account(request, id, token):
    """
    Activate user account based on the provided activation token.

    Parameters:
        request (HttpRequest): The HTTP request object.
        id (int): The ID of the user whose account is to be activated.
        token (str): The activation token associated with the user.

    Returns:
        JsonResponse: A JSON response with the activation result message.

    Raises:
        None.

    Description:
        This view function handles the activation of a user's account based on the
        provided activation token. The function checks if the HTTP request method is
        "GET". If it is, it attempts to activate the user's account using the given
        user ID and token. If the activation is successful, a JSON response with a
        success message is returned. If the activation token is invalid, an error
        message indicating an invalid activation link is returned. If the user with
        the given ID does not exist, a message indicating that the user does not
        exist is returned.

        If the HTTP request method is not "GET", an "Invalid request" message is
        returned in a JSON response.

    Example:
        # Assuming the view is mapped to the URL path '/activate/<int:id>/<str:token>/'
        # and a user with the given ID and token exists, the account will be activated
        # and the response will be:
        # {"Message": "Your account has been activated successfully!"}
    """


    if request.method == "GET":
        try:
            user = User.objects.get(id=id)
            if default_token_generator.check_token(user, token):
                return JsonResponse({"Message": "Your account has been activated successfully!"})
            else:
                return JsonResponse({"Message": "Invalid activation link"})
        except User.DoesNotExist:
            return JsonResponse({"Message": "User does not exist"})
    
    return JsonResponse({"Message": "Invalid request"})
