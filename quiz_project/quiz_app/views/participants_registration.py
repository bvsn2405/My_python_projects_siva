import json

from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from quiz_app.utilities.validations import validate_username, validate_password


@csrf_exempt
def participants_reg(request):
    """
    View function to register participants.

    Accepts a POST request with participant registration data in JSON format.
    Checks if a user with the provided username already exists.
    If the user does not exist, creates a new user with the provided registration data.
    Hashes the user's password using Django's `make_password` function.
    Returns a JSON response indicating the status of the registration process.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        JsonResponse: JSON response with a message indicating the status of the registration process.

    Example Usage:
        - Request URL: POST /participants/reg/
        - Request Body:
            {
                "username": "siva@123",
                "first_name": "Siva",
                "last_name": "Ram",
                "email": "siva@gmail.com",
                "password": "Password@123"
            }
        - Response (New User):
            {
                "message": "user registration done successfully"
            }
        - Response (User Already Exists):
            {
                "message": "user already exist"
            }
    """

    if request.method == "POST":
        data = json.loads(request.body)
        try:
            valid_username = validate_username(data['username'])
            valid_password = validate_password(data['password'])
            if User.objects.filter(username=data['username']).exists():
                return JsonResponse({"message": "user already exist"}, status=400)
            else:
                if valid_username is True and valid_password is True:
                    User.objects.create(
                        username=data['username'],
                        first_name=data['first_name'],
                        last_name=data['last_name'],
                        email=data['email'],
                        password=make_password(data['password']))
                    return JsonResponse({"message": "user registration done successfully"})
                else:
                    errors = []
                    if valid_username is not True:
                        errors.extend(valid_username)
                    if valid_password is not True:
                        errors.extend(valid_password)
                    return JsonResponse({"Error message": errors}, status=400)
        except:
            return JsonResponse({"Error message": "Invalid data submitted"}, status=400)


    return JsonResponse({"message": "Invalid request"}, status=400)
