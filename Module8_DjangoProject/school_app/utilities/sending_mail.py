from django.core.mail import send_mail

def sending_mail(to_email,otp):
    subject = 'OTP to reset Password'
    from_email = 'settings.EMAIL_HOST_USER'
    message = f"otp for resetting password is : {otp}"
    send_mail(subject, message, from_email, [to_email])
