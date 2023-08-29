from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User


def update_user(id, username, password, first_name, last_name, email):
    User.objects.filter(id=id).update(
        username=username,
        first_name=first_name,
        last_name=last_name,
        email=email,
        password=make_password(password))
