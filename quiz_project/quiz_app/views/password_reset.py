import json

from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def password_reset(request):
    """
    This view function is for Reset the user's password.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        JsonResponse: A JSON response with a message indicating whether the password
                      was updated successfully or if the user does not exist.

    Description:
        This view function handles the password reset process. It expects a POST request
        containing the user's new password in JSON format. If the request is valid and
        the user exists, the function updates the user's password to the new password
        provided by the user.

        If the user does not exist, a message indicating that the user does not exist
        is returned.

    Example:
        # Assuming the view is mapped to the URL path '/password_reset/' and the
        # provided password is successfully updated, the response will be:
        # {"message": "password updated successfully !"}
    """
    try:
        if request.method == "POST":
            user = User.objects.get(username=request.user.username)

            try:
                data = json.loads(request.body)
                password = data['new_password']
                user.password = make_password(password)
                user.save()
                return JsonResponse({"message": "password updated successfully ! "})
            except:
                return JsonResponse({"message": "Invalid data provided !"},status=400)


    except:
        return JsonResponse({"message": "Invalid request method"}, status=400)
    return JsonResponse({"message": "Invalid request method"}, status=400)
