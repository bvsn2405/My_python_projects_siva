from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.contrib.auth.models import User
from school_app.models.students import Students
from django.contrib.auth.tokens import default_token_generator
from django.urls import reverse

@receiver(post_save, sender=Students)
def send_registration_email(sender, instance, created, **kwargs):
    if created:
        user = User.objects.get(id=instance.user_id)
        token = default_token_generator.make_token(user)
        domain = '127.0.0.1:8000'
        protocol = 'http'
        activation_url = reverse('activate', kwargs={'token': token})
        activation_url = f'{protocol}://{domain}{activation_url}'

        subject = 'Registration Successful'
        message = f"Dear {instance.name},\n\nThank you for registering!\n\nPlease click the link below to activate your account:\n\n{activation_url}\n\nBest regards,\nYour school_app Team"
        from_email = 'settings.EMAIL_HOST_USER'
        to_email = user.email

        send_mail(subject, message, from_email, [to_email])
