import json
from datetime import datetime

import pytest
from django.contrib.auth.models import User
from online_auction_app.models.Items import Items
from online_auction_app.models.auction_won import Auction_won
from rest_framework.test import APIClient

client = APIClient()


@pytest.mark.django_db(transaction=True)
def test_submit_ratings_success(create_item, create_user_admin):
    client.post('/online_auction/login/', json.dumps({"username": "admin", "password": "admin"}),
                content_type='application/json')

    Auction_won.objects.create(auction_won_by=create_user_admin, item=create_item, amount=5000)

    client.post('/online_auction/payment/1/', data=json.dumps({"amount": 5000}),
                content_type='application/json')

    data = {"rating": 8, "review": "average product1"}

    response = client.post("/online_auction/submit_rating/1/",
                           data=json.dumps(data), content_type='application/json')

    assert response.status_code == 200
    assert response.json() == {"message": "Rating and review for the product submitted successfully!"}


@pytest.mark.django_db(transaction=True)
def test_submit_ratings_success2(create_item, create_user_admin):
    client.post('/online_auction/login/', json.dumps({"username": "admin", "password": "admin"}),
                content_type='application/json')

    Auction_won.objects.create(auction_won_by=create_user_admin, item=create_item, amount=5000)

    client.post('/online_auction/payment/1/', data=json.dumps({"amount": 5000}),
                content_type='application/json')

    data = {"rating": 8, "review": "average product1"}

    client.post("/online_auction/submit_rating/1/",
                data=json.dumps(data), content_type='application/json')

    data = {"rating": 4, "review": "average product"}

    response = client.post("/online_auction/submit_rating/1/",
                           data=json.dumps(data), content_type='application/json')

    assert response.status_code == 200
    assert response.json() == {"message": "Rating and review for the product updated successfully!"}


@pytest.mark.django_db(transaction=True)
def test_submit_ratings_without_payment(create_item, create_user_admin):
    Auction_won.objects.create(auction_won_by=create_user_admin, item=create_item, amount=5000)
    Auction_won.objects.create(auction_won_by=create_user_admin, item=create_item, amount=1000)
    time_now = datetime.now()
    item = Items.objects.create(
        title='Title',
        description='Description',
        image="siva.jpg",
        starting_price=100,
        seller=create_user_admin,
        auction_end_time=time_now,
        is_active=True)
    user = User.objects.create_user(username="siva", password='siva')
    auction = Auction_won.objects.create(
        auction_won_by=user,
        item=item,
        amount=100)

    res = client.post('/online_auction/login/', json.dumps({"username": "siva", "password": "siva"}),
                      content_type='application/json')
    assert res.status_code == 200

    data = {"rating": 4, "review": "average product"}

    response = client.post("/online_auction/submit_rating/2/",
                           data=json.dumps(data), content_type='application/json')

    assert response.status_code == 400
    assert response.json() == {"message": "You have to make payment for the item before you rate it!!"}
    assert auction.auction_won_by.username == 'siva'


@pytest.mark.django_db(transaction=True)
def test_submit_ratings_invalid_data(create_item, create_user_admin):
    client.post('/online_auction/login/', json.dumps({"username": "admin", "password": "admin"}),
                content_type='application/json')

    Auction_won.objects.create(auction_won_by=create_user_admin, item=create_item, amount=5000)

    client.post('/online_auction/payment/1/', data=json.dumps({"amount": 5000}),
                content_type='application/json')

    data = {}

    response = client.post("/online_auction/submit_rating/1/",
                           data=json.dumps(data), content_type='application/json')

    assert response.status_code == 400
    assert response.json() == {"message": "Invalid rating provided"}


@pytest.mark.django_db(transaction=True)
def test_submit_ratings_invalid_data2(create_item, create_user_admin):
    client.post('/online_auction/login/', json.dumps({"username": "admin", "password": "admin"}),
                content_type='application/json')

    Auction_won.objects.create(auction_won_by=create_user_admin, item=create_item, amount=5000)

    client.post('/online_auction/payment/1/', data=json.dumps({"amount": 5000}),
                content_type='application/json')

    response = client.post("/online_auction/submit_rating/1/",
                           content_type='application/json')

    assert response.status_code == 400
    assert response.json() == {"message": "Invalid JSON data provided"}


@pytest.mark.django_db(transaction=True)
def test_submit_ratings_to_others_auction(create_item, create_user_admin):
    Auction_won.objects.create(auction_won_by=create_user_admin, item=create_item, amount=5000)
    Auction_won.objects.create(auction_won_by=create_user_admin, item=create_item, amount=1000)
    time_now = datetime.now()
    item = Items.objects.create(
        title='Title',
        description='Description',
        image="siva.jpg",
        starting_price=100,
        seller=create_user_admin,
        auction_end_time=time_now,
        is_active=True)
    user = User.objects.create_user(username="siva", password='siva')
    auction = Auction_won.objects.create(
        auction_won_by=user,
        item=item,
        amount=100)

    res = client.post('/online_auction/login/', json.dumps({"username": "admin", "password": "admin"}),
                      content_type='application/json')

    data = {"rating": 4, "review": "average product"}

    response = client.post("/online_auction/submit_rating/2/",
                           data=json.dumps(data), content_type='application/json')

    assert response.status_code == 400
    assert response.json() == {"message": "The Auction belongs to others!"}


@pytest.mark.django_db(transaction=True)
def test_submit_ratings_auction_does_not_exist(create_item, create_user_admin):
    client.post('/online_auction/login/', json.dumps({"username": "admin", "password": "admin"}),
                content_type='application/json')

    Auction_won.objects.create(auction_won_by=create_user_admin, item=create_item, amount=5000)

    client.post('/online_auction/payment/1/', data=json.dumps({"amount": 5000}),
                content_type='application/json')

    data = {"rating": 8, "review": "average product1"}

    response = client.post("/online_auction/submit_rating/12341/",
                           data=json.dumps(data), content_type='application/json')

    assert response.status_code == 400
    assert response.json() == {"message": "The Auction does not exist!"}

