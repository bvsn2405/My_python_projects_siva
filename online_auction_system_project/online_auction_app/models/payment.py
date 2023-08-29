from django.contrib.auth.models import User
from django.db import models
from .Items import Items


class Payment(models.Model):
    """
       Represents a payment for an item in the auction.

       Attributes:
           buyer (User): The person making the payment.
           item (Item): The item for which the payment is made.
           payment_done (bool): Whether the payment has been completed.
           amount (int): The amount paid for the item.

       Note:
           - This model tracks payments for items won in the auction.
           - `buyer` refers to the person who won the item in the auction making the payment.
           - `item` is the item being paid for.
           - `payment_done` indicates if the payment is finished.
       """
    buyer = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Items, on_delete=models.CASCADE)
    payment_done = models.BooleanField()
    amount = models.IntegerField()
