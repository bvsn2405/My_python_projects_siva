import json
from online_auction_app.models.Items import Items
from online_auction_app.models.auction_won import Auction_won
from online_auction_app.models.Bid import Bid
from online_auction_app.models.Automatic_Bid import Automatic_Bid
from online_auction_app.models.payment import Payment

import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient

client = APIClient()
from datetime import datetime, timedelta


@pytest.mark.django_db(transaction=True)
def test_update_inactive_auction_status(create_user_admin):
    user1 = User.objects.create_user(username='admin1', password='admin1', email='admin@gmail.com')
    user2 = User.objects.create_user(username='admin2', password='admin2', email='admin@gmail.com')
    user3 = User.objects.create_user(username='admin3', password='admin3', email='admin@gmail.com')
    user4 = User.objects.create_user(username='admin4', password='admin4', email='admin@gmail.com')

    time_now = datetime.now()
    item1 = Items.objects.create(title='Title', description='Description', image="siva.jpg",
                                 starting_price=100, seller=create_user_admin, auction_end_time=time_now,
                                 is_active=True)
    item2 = Items.objects.create(title='Title', description='Description', image="siva.jpg",
                                 starting_price=100, seller=create_user_admin, auction_end_time=time_now,
                                 is_active=True)
    item3 = Items.objects.create(title='Title', description='Description', image="siva.jpg",
                                 starting_price=100, seller=create_user_admin, auction_end_time=time_now,
                                 is_active=True)
    item4 = Items.objects.create(title='Title', description='Description', image="siva.jpg",
                                 starting_price=100, seller=create_user_admin, auction_end_time=time_now - timedelta(1),
                                 is_active=True)

    Bid.objects.create(user=user1, item=item1, bid_amount=1000, bid_time=time_now)
    Bid.objects.create(user=user2, item=item1, bid_amount=1100, bid_time=time_now)
    Bid.objects.create(user=user3, item=item1, bid_amount=1200, bid_time=time_now)
    Bid.objects.create(user=user4, item=item1, bid_amount=900, bid_time=time_now)

    Bid.objects.create(user=user1, item=item2, bid_amount=1000, bid_time=time_now)
    Bid.objects.create(user=user2, item=item2, bid_amount=1100, bid_time=time_now)
    Bid.objects.create(user=user3, item=item2, bid_amount=1200, bid_time=time_now)
    Bid.objects.create(user=user4, item=item2, bid_amount=900, bid_time=time_now)

    Automatic_Bid.objects.create(user=user1, item=item1, max_bid_amount=1500, bid_time=time_now)
    Automatic_Bid.objects.create(user=user2, item=item1, max_bid_amount=1400, bid_time=time_now)
    Automatic_Bid.objects.create(user=user3, item=item1, max_bid_amount=1300, bid_time=time_now)
    Automatic_Bid.objects.create(user=user4, item=item1, max_bid_amount=1200, bid_time=time_now)

    Automatic_Bid.objects.create(user=user1, item=item1, max_bid_amount=1600, bid_time=time_now)
    Automatic_Bid.objects.create(user=user2, item=item1, max_bid_amount=1700, bid_time=time_now)
    Automatic_Bid.objects.create(user=user3, item=item1, max_bid_amount=1800, bid_time=time_now)
    Automatic_Bid.objects.create(user=user4, item=item1, max_bid_amount=1900, bid_time=time_now)

    Bid.objects.create(user=user1, item=item1, bid_amount=1000, bid_time=time_now)
    Bid.objects.create(user=user2, item=item1, bid_amount=1100, bid_time=time_now)
    Bid.objects.create(user=user3, item=item1, bid_amount=1200, bid_time=time_now)
    Bid.objects.create(user=user4, item=item1, bid_amount=900, bid_time=time_now)

    Auction_won.objects.create(auction_won_by=create_user_admin,item=item1,amount=100)

    res1 = client.get('/online_auction/update_auctions_status/')

    assert res1.status_code == 200

    item1.is_active = False
    item2.is_active = False
    item3.is_active = False
    item1.save()
    item2.save()
    item3.save()

    res2 = client.get('/online_auction/update_auctions_status/')

    assert res2.status_code == 200
    assert item4.is_active == True


@pytest.mark.django_db(transaction=True)
def test_update_inactive_auction_status_invalid_request_method():
    response = client.post('/online_auction/update_auctions_status/')

    assert response.status_code == 405
    assert response.json() == {"message": "Invalid request method"}
