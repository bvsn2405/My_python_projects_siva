from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sessions.backends.db import SessionStore
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=User)
def send_registration_email(sender, instance, created, **kwargs):
    if created:
        token = default_token_generator.make_token(instance)
        domain = '127.0.0.1:8000'
        protocol = 'http'
        activation_url = f'{protocol}://{domain}/quiz/activate/{instance.id}/{token}/'

        request = kwargs.get('request')
        if request:
            session = SessionStore(request)
            session['activation_id'] = instance.id
            session['activation_token'] = token
            session.save()

        subject = 'Registration Successful'
        message = f"Dear {instance.username},\n\nThank you for registering!\n\nPlease click the link below to " \
                  f"activate your account:\n\n{activation_url}\n\nBest regards,\nYour school_app Team"
        from_email = 'settings.EMAIL_HOST_USER'
        to_email = instance.email

        send_mail(subject, message, from_email, [to_email])
