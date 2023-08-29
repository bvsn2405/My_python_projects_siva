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
def test_auctions_closed(create_user_admin):
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

    Bid.objects.create(user=user1, item=item3, bid_amount=1000, bid_time=time_now)
    Bid.objects.create(user=user2, item=item3, bid_amount=1100, bid_time=time_now)
    Bid.objects.create(user=user3, item=item3, bid_amount=1200, bid_time=time_now)
    Bid.objects.create(user=user4, item=item3, bid_amount=900, bid_time=time_now)

    client.get('/online_auction/update_auctions_status/')

    item1.is_active = False
    item2.is_active = False
    item3.is_active = False
    item1.save()
    item2.save()
    item3.save()
    response = client.get('/online_auction/auctions_closed/')
    assert response.status_code == 200


@pytest.mark.django_db(transaction=True)
def test_auctions_closed_failed_condition(create_user_admin):
    response = client.get('/online_auction/auctions_closed/')
    assert response.status_code == 200


@pytest.mark.django_db(transaction=True)
def test_auctions_closed_invalid_request_method_post():
    response = client.post('/online_auction/auctions_closed/')
    assert response.status_code == 405
    assert response.json() == {"message": "Invalid request method"}


@pytest.mark.django_db(transaction=True)
def test_auctions_closed_invalid_request_method_put():
    response = client.put('/online_auction/auctions_closed/')
    assert response.status_code == 405
    assert response.json() == {"message": "Invalid request method"}


@pytest.mark.django_db(transaction=True)
def test_auctions_closed_invalid_request_method_patch():

    response = client.patch('/online_auction/auctions_closed/')
    assert response.status_code == 405
    assert response.json() == {"message": "Invalid request method"}


@pytest.mark.django_db(transaction=True)
def test_auctions_closed_invalid_request_method_delete():
    response = client.delete('/online_auction/auctions_closed/')
    assert response.status_code == 405
    assert response.json() == {"message": "Invalid request method"}
