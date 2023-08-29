from django.contrib.auth.models import User
from django.db import models
from .Items import Items


class Auction_won(models.Model):
    """
       Represents a users who won the auction for an item .

       Attributes:
           auction_won_by (User): The person who won the auction.
           item (Item): The item for which the payment is made.
           amount (int): The amount paid for the item.

       Note:
           - `buyer` refers to the person who won the item in the auction making the payment.
           - `item` is the item being paid for.
       """
    auction_won_by = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Items, on_delete=models.CASCADE)
    amount = models.IntegerField()

