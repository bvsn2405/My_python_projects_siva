import json

from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from quiz_app.utilities.validations import validate_password, validate_username


@csrf_exempt
def update_participant_data(request):
    """
    View function to update participant data.

    Accepts a PUT or PATCH request with participant data in JSON format to update the user with the provided ID.
    If the request is a PUT request, the function updates all fields of the user with the provided data.
    If the request is a PATCH request, the function updates only the fields specified in the request data.

    Args:
        request (HttpRequest): The HTTP request object.
        id (int): The ID of the user whose data is to be updated.

    Returns:
        JsonResponse: JSON response with a message indicating the status of the update process.

    Example Usage (PUT Request):
        - Request URL: PUT /participants/update/1/ (where '1' is the ID of the user)
        - Request Body:
            {
                "username": "new_username",
                "first_name": "New First Name",
                "last_name": "New Last Name",
                "email": "new_email@example.com",
                "password": "new_secure_password"
            }
        - Response:
            {
                "message": "User data updated successfully"
            }

    Example Usage (PATCH Request):
        - Request URL: PATCH /participants/update/1/ (where '1' is the ID of the user)
        - Request Body (Update Username and Email):
            {
                "username": "new_username",
                "email": "new_email@example.com"
            }
        - Response:
            {
                "message": "User Data updated successfully"
            }

    Note:
        - For PUT requests, all user data fields must be provided in the request body.
        - For PATCH requests, only the fields that need to be updated should be included in the request body.
        - The user's password will be hashed using Django's `make_password` function before saving the update.
    """
    if request.method == 'PUT':
        user = User.objects.get(username=request.user.username)
        data = json.loads(request.body)
        try:
            username = data['username']
            password = data['password']
            valid_username = validate_username(username)
            valid_password = validate_password(password)
            if valid_username is True and valid_password is True:
                user.username = username
                user.password = make_password(password)
                user.first_name = data['first_name']
                user.last_name = data['last_name']
                user.email = data['email']
                user.save()
                return JsonResponse({'message': 'User data updated successfully'})
            else:
                errors = []
                if valid_username is not True:
                    errors.extend(valid_username)
                if valid_password is not True:
                    errors.extend(valid_password)
                return JsonResponse({"Error message": errors}, status=400)
        except:
            return JsonResponse({'message': 'Invalid Data'}, status=400)

    elif request.method == 'PATCH':
        user = User.objects.get(username=request.user.username)
        data = json.loads(request.body)

        fields_to_check = ['username', 'password', 'email', 'first_name', 'last_name']
        fields_exist = [key in data for key in fields_to_check]

        if any(fields_exist):
            errors = []

            if 'username' in data:
                valid_username = validate_username(data['username'])
                if valid_username is True:
                    user.username = data['username']
                else:
                    errors.extend(valid_username)
            if 'email' in data:
                user.email = data['email']
            if 'password' in data:
                valid_password = validate_password(data['password'])
                if valid_password is True:
                    user.password = make_password(data['password'])
                else:
                    errors.extend(valid_password)

            if 'first_name' in data:
                user.first_name = data['first_name']
            if 'last_name' in data:
                user.last_name = data['last_name']

            if errors:
                return JsonResponse({"Error message": errors}, status=400)
            user.save()
            return JsonResponse({'message': 'User Data updated successfully'})
        else:
            return JsonResponse({'message': 'Invalid Data'}, status=400)
    else:
        return JsonResponse({"Message": "Invalid request method"}, status=400)
