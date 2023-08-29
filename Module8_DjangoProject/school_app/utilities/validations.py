import re
from django.contrib.auth.models import User
def validate_name(name):
    if not name:
        return ['Name should not be empty']
    elif len(name)<4:
        return ['Name should not less than 4 characters']
    elif len(name)>40:
        return ['Name should not more than 40 characters']
    return True

def validate_username(username):
    if not username:
        return ['Username should not be empty']
    if len(username)<4:
        return ['Username should not less than 4 characters']
    if not re.match(r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[@#$%^&.+=])[A-Za-z\d@#$%^&.+=]+$', username):
        return ['Username should contain at least one alphabet, one numeric character, and one special character.']

    return True
        

def validate_password(password):
    if not password:
        return ['Password should not be empty']
    if len(password)<4:
        return ['Password should not less than 4 characters']
    if not re.match(r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[@#$%^&.+=])[A-Za-z\d@#$%^&.+=]+$', password):
        return ['Password should contain at least one alphabet, one numeric character, and one special character.']

    return True

