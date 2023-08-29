from django.contrib.auth.models import User
from django.db import models

from .Items import Items


class Automatic_Bid(models.Model):
    """
        Represents a maximum bid placed by a user on an item.

        Attributes:
            user (User): The user placing the bid.
            item (Item): The item for which the bid is placed.
            max_bid_amount (int): The maximum amount the user is bidding for the item.

        Note:
        - Automatic bids are placed on behalf of the user up to their maximum bid amount.
        """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Items, on_delete=models.CASCADE)
    max_bid_amount = models.IntegerField()
    bid_time = models.DateTimeField(default=None)

