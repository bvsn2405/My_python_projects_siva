import json

from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from quiz_app.utilities.generate_otp import generate_otp
from quiz_app.utilities.sending_mail import sending_mail


@csrf_exempt
def forgot_password(request):
    """
    Send a one-time password (OTP) to the user's email for password reset.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        JsonResponse: A JSON response with a message indicating whether the OTP
                      was sent successfully or if the user does not exist.

    Description:
        This view function handles the process of sending a one-time password (OTP)
        to the user's email for password reset. It expects a POST request containing
        the user's username in JSON format. If a user with the provided username
        exists, an OTP is generated and sent to the user's email. The OTP is stored
        in the session for later verification during the password reset process.

        If the provided username does not match any user in the database, a message
        indicating that the user does not exist is returned.

    Example:
        # Assuming the view is mapped to the URL path '/forgot_password/' and a
        # user with the given username exists, the response will be:
        # {"message": "OTP sent to your mail successfully"}
    """
    try:
        if request.method == "POST":

            data = json.loads(request.body)
            try:
                username=data['username']
                try:
                    user = User.objects.get(username=username)
                    to_mail = user.email
                    otp = generate_otp()
                    request.session['otp'] = otp
                    request.session.modified = True
                    sending_mail(otp=otp, to_email=to_mail)
                    return JsonResponse({"message": "OTP sent to your mail successfully"})
                except:
                    return JsonResponse({"message": "User does not exist"},status=400)
            except:
                return JsonResponse({"message": "Invalid data"}, status=400)
    except:
        return JsonResponse({"message": "Invalid request method"},status=400)

    return JsonResponse({"message": "Invalid request method"},status=400)


@csrf_exempt
def forgot_password_otp_validation(request):
    """
    Validate the one-time password (OTP) provided by the user and update the password.

    Accepts a POST request with JSON data containing the details of the question.
    The user must be a superuser to add a question.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        JsonResponse: A JSON response with a message indicating whether the OTP
                      was valid and the password was updated successfully, or if
                      the user does not exist.
    JSON Data Format:
        {
            "username": "username of the user",
            "options": "OTP sent to email",
            "new_password": "enter the new password"
        }

    Example Usage:
        - Request URL: POST /quiz/forgot_password/otp_validation/
        - Request Body:
            {
                
            "username": "username123",
            "options": "233231",
            "new_password": "Password@123"
        
            }

    """

    if request.method == "POST":
        data = json.loads(request.body)
        otp_mail = data['otp']
        try:
            user = User.objects.get(username=data['username'])
            otp = request.session.get('otp')

            if otp == otp_mail:
                user.password = make_password(data['password'])
                user.save()
                return JsonResponse({"message": "Password updated successfully !"})
            else:
                return JsonResponse({"message": "Invalid OTP"})
        except:
            return JsonResponse({"message": "User does not exist"})
    return JsonResponse({"message": "Invalid request"}, status=404)
