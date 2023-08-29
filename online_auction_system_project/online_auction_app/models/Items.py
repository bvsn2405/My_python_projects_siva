from django.contrib.auth.models import User
from django.db import models

class Items(models.Model):
    """
        Represents an item that can be put up for auction.

        Attributes:
            title (str): The name of the item.
            description (str): A detailed description of the item.
            image (ImageField): An image showing what the item looks like.
            starting_price (int): The initial price for bidding on the item.
            seller (User): The person who is selling the item.
            auction_end_time (datetime): When the auction is set to finish.
            is_active (bool): Whether the auction is currently running or not.

        Note:
            - The `image` field holds the path to the uploaded image.
            - The `auction_end_time` field marks when the bidding will end.
            - The `is_active` field tells if the auction is still ongoing.
        """
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='item_images/')
    starting_price = models.IntegerField()
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    auction_end_time = models.DateTimeField()
    is_active = models.BooleanField(default=True)
