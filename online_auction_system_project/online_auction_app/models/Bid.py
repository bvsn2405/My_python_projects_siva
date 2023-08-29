from django.contrib.auth.models import User
from django.db import models
from .Items import Items


class Bid(models.Model):
    """
        Represents a bid placed by a user on an item.

        Attributes:
            user (User): The user placing the bid.
            item (Item): The item for which the bid is placed.
            bid_amount (int): The amount the user is bidding for the item.
            bid_time (datetime): The date and time when the bid was placed.

        Note:
            - Bids are placed manually by users.
        """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Items, on_delete=models.CASCADE)
    bid_amount = models.IntegerField()
    bid_time = models.DateTimeField()
