from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver

from ..models.auction_won import Auction_won


@receiver(post_save, sender=Auction_won)
def send_registration_email(sender, instance, created, **kwargs):
    item = instance.item
    user = instance.auction_won_by
    if created:
        subject = 'Congratulations you won the Auction'
        message = f"You have participated in the Auction no:{item.id} and won the item {item.title}. " \
                  f"Its price is {instance.amount}.please make the payment to get that item."
        from_email = 'settings.EMAIL_HOST_USER'
        to_email = user.email

        send_mail(subject, message, from_email, [to_email])
