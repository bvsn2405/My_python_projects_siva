from django.contrib.auth.models import User
from django.db import models
from .Items import Items


class Ratings(models.Model):
    """
       Represents a review and rating for an item from a buyer.

       Attributes:
           buyer (User): The person writing the review and rating.
           item (Item): The item being reviewed and rated.
           review (str): The written feedback about the item.
           rating (int): The numeric rating given by the buyer.

       Note:
           - This model holds reviews and ratings for items.
           - `buyer` is the person writing the review and rating.
           - `item` is the item being reviewed.
           - `review` contains written feedback about the item.
           - `rating` is the numeric rating given by the buyer.
       """
    buyer = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Items, on_delete=models.CASCADE)
    review = models.TextField()
    rating = models.IntegerField()
