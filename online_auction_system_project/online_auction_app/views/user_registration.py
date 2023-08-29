import json

from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from ..utilities.validations import validate_username, validate_password


class UserRegistrationView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def post(self, request):
        try:
            data = json.loads(request.body)
            valid_username = validate_username(data['username'])
            valid_password = validate_password(data['password'])

            if User.objects.filter(username=data['username']).exists():
                return JsonResponse({"message": "user already exists"}, status=400)
            else:
                if valid_username is True and valid_password is True:
                    User.objects.create(
                        username=data['username'],
                        first_name=data['first_name'],
                        last_name=data['last_name'],
                        email=data['email'],
                        password=make_password(data['password'])
                    )
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

    def get(self, request):
        return JsonResponse({"message": "Invalid request method"}, status=405)

    def put(self, request):
        return JsonResponse({"message": "Invalid request method"}, status=405)

    def patch(self, request):
        return JsonResponse({"message": "Invalid request method"}, status=405)

    def delete(self, request):
        return JsonResponse({"message": "Invalid request method"}, status=405)
