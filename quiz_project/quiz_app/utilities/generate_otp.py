import random
import string


def generate_otp():
    characters = string.digits
    otp = ''.join(random.choice(characters) for _ in range(6))
    return otp


