import json
from datetime import datetime

import pytest
from django.contrib.auth.models import User
from online_auction_app.models.Items import Items
from online_auction_app.models.auction_won import Auction_won
from rest_framework.test import APIClient

client = APIClient()


@pytest.mark.django_db(transaction=True)
def test_payment_to_auction_won_success():
    user = User.objects.create_user(username='admin', password='admin', email='admin@gmail.com')
    client.post('/online_auction/login/', data=json.dumps({"username": "admin", "password": "admin"}),
                content_type="application/json")
    time_now = datetime.now()
    item = Items.objects.create(
        title='Title',
        description='Description',
        image="siva.jpg",
        starting_price=100,
        seller=user,
        auction_end_time=time_now,
        is_active=True)
    Auction_won.objects.create(auction_won_by=user, item=item, amount=5000)

    response = client.post('/online_auction/payment/1/', data=json.dumps({"amount": 5000}),
                           content_type='application/json')
    assert response.status_code == 200
    assert response.json() == {"message": "Payment done successfully !"}
    assert Auction_won.objects.filter(id=1).exists()


@pytest.mark.django_db(transaction=True)
def test_payment_to_auction_won_fail_condition_1():
    user = User.objects.create_user(username='admin', password='admin', email='admin@gmail.com')
    client.post('/online_auction/login/', data=json.dumps({"username": "admin", "password": "admin"}),
                content_type="application/json")
    time_now = datetime.now()
    item = Items.objects.create(
        title='Title',
        description='Description',
        image="siva.jpg",
        starting_price=100,
        seller=user,
        auction_end_time=time_now,
        is_active=True)
    Auction_won.objects.create(auction_won_by=user, item=item, amount=5000)

    client.post('/online_auction/payment/1/', data=json.dumps({"amount": 5000}),
                content_type='application/json')
    response = client.post('/online_auction/payment/1/', data=json.dumps({"amount": 5000}),
                           content_type='application/json')
    assert response.status_code == 400
    assert response.json() == {"message": "Already payment done !"}


@pytest.mark.django_db(transaction=True)
def test_payment_to_auction_won_fail_condition_2():
    user = User.objects.create_user(username='admin', password='admin', email='admin@gmail.com')
    client.post('/online_auction/login/', data=json.dumps({"username": "admin", "password": "admin"}),
                content_type="application/json")
    time_now = datetime.now()
    item = Items.objects.create(
        title='Title',
        description='Description',
        image="siva.jpg",
        starting_price=100,
        seller=user,
        auction_end_time=time_now,
        is_active=True)
    auction = Auction_won.objects.create(auction_won_by=user, item=item, amount=5000)

    data = {"amount": 4000}
    response = client.post('/online_auction/payment/1/', json.dumps(data), content_type='application/json')
    amount_received = data['amount']
    assert response.status_code == 400
    assert response.json() == {"message": "Payment failed",
                               "error message": f"You have to pay: {auction.amount},but you paid: {amount_received}"}


@pytest.mark.django_db(transaction=True)
def test_payment_to_auction_won_fail_condition_3():
    user = User.objects.create_user(username='admin', password='admin', email='admin@gmail.com')
    client.post('/online_auction/login/', data=json.dumps({"username": "admin", "password": "admin"}),
                content_type="application/json")
    time_now = datetime.now()
    item = Items.objects.create(
        title='Title',
        description='Description',
        image="siva.jpg",
        starting_price=100,
        seller=user,
        auction_end_time=time_now,
        is_active=True)
    Auction_won.objects.create(auction_won_by=user, item=item, amount=5000)

    data = {"amounts": 4000}
    response = client.post('/online_auction/payment/1/', json.dumps(data), content_type='application/json')
    assert response.status_code == 400
    assert response.json() == {"message": "Invalid data provided !"}


@pytest.mark.django_db(transaction=True)
def test_payment_to_auction_won_fail_condition_4():
    user = User.objects.create_user(username='admin', password='admin', email='admin@gmail.com')
    user2 = User.objects.create_user(username='admin1', password='admin1', email='admin@gmail.com')

    client.post('/online_auction/login/', data=json.dumps({"username": "admin1", "password": "admin1"}),
                content_type="application/json")
    time_now = datetime.now()
    item = Items.objects.create(
        title='Title',
        description='Description',
        image="siva.jpg",
        starting_price=100,
        seller=user,
        auction_end_time=time_now,
        is_active=True)
    Auction_won.objects.create(auction_won_by=user, item=item, amount=5000)

    data = {"amounts": 4000}
    response = client.post('/online_auction/payment/1/', json.dumps(data), content_type='application/json')
    assert response.status_code == 400
    assert response.json() == {"message": "The auction does not won by you! It belongs to others"}



@pytest.mark.django_db(transaction=True)
def test_payment_to_auction_won_fail_condition_5():
    user = User.objects.create_user(username='admin', password='admin', email='admin@gmail.com')
    user2 = User.objects.create_user(username='admin1', password='admin1', email='admin@gmail.com')

    client.post('/online_auction/login/', data=json.dumps({"username": "admin1", "password": "admin1"}),
                content_type="application/json")
    time_now = datetime.now()
    item = Items.objects.create(
        title='Title',
        description='Description',
        image="siva.jpg",
        starting_price=100,
        seller=user,
        auction_end_time=time_now,
        is_active=True)
    Auction_won.objects.create(auction_won_by=user, item=item, amount=5000)

    data = {"amounts": 4000}
    response = client.post('/online_auction/payment/11/', json.dumps(data), content_type='application/json')
    assert response.status_code == 400
    assert response.json() == {"message": "The auction does not exists"}


@pytest.mark.django_db(transaction=True)
def test_payment_to_auction_won_invalid_request_method_get():
    user = User.objects.create_user(username='admin', password='admin', email='admin@gmail.com')

    client.post('/online_auction/login/', data=json.dumps({"username": "admin", "password": "admin"}),
                content_type="application/json")
    time_now = datetime.now()
    item = Items.objects.create(
        title='Title',
        description='Description',
        image="siva.jpg",
        starting_price=100,
        seller=user,
        auction_end_time=time_now,
        is_active=True)
    Auction_won.objects.create(auction_won_by=user, item=item, amount=5000)

    response = client.get('/online_auction/payment/1/')
    assert response.status_code == 405
    assert response.json() == {"message": "Invalid request method"}


@pytest.mark.django_db(transaction=True)
def test_payment_to_auction_won_invalid_request_method_put():
    user = User.objects.create_user(username='admin', password='admin', email='admin@gmail.com')
    user2 = User.objects.create_user(username='admin1', password='admin1', email='admin@gmail.com')

    client.post('/online_auction/login/', data=json.dumps({"username": "admin1", "password": "admin1"}),
                content_type="application/json")
    time_now = datetime.now()
    item = Items.objects.create(
        title='Title',
        description='Description',
        image="siva.jpg",
        starting_price=100,
        seller=user,
        auction_end_time=time_now,
        is_active=True)
    Auction_won.objects.create(auction_won_by=user, item=item, amount=5000)

    data = {"amounts": 4000}
    response = client.put('/online_auction/payment/11/', json.dumps(data), content_type='application/json')
    assert response.status_code == 405
    assert response.json() == {"message": "Invalid request method"}


@pytest.mark.django_db(transaction=True)
def test_payment_to_auction_won_invalid_request_method_patch():
    user = User.objects.create_user(username='admin', password='admin', email='admin@gmail.com')
    user2 = User.objects.create_user(username='admin1', password='admin1', email='admin@gmail.com')

    client.post('/online_auction/login/', data=json.dumps({"username": "admin1", "password": "admin1"}),
                content_type="application/json")
    time_now = datetime.now()
    item = Items.objects.create(
        title='Title',
        description='Description',
        image="siva.jpg",
        starting_price=100,
        seller=user,
        auction_end_time=time_now,
        is_active=True)
    Auction_won.objects.create(auction_won_by=user, item=item, amount=5000)

    data = {"amounts": 4000}
    response = client.patch('/online_auction/payment/11/', json.dumps(data), content_type='application/json')
    assert response.status_code == 405
    assert response.json() == {"message": "Invalid request method"}


@pytest.mark.django_db(transaction=True)
def test_payment_to_auction_won_invalid_request_method_delete():
    user = User.objects.create_user(username='admin', password='admin', email='admin@gmail.com')

    client.post('/online_auction/login/', data=json.dumps({"username": "admin", "password": "admin"}),
                content_type="application/json")
    time_now = datetime.now()
    item = Items.objects.create(
        title='Title',
        description='Description',
        image="siva.jpg",
        starting_price=100,
        seller=user,
        auction_end_time=time_now,
        is_active=True)
    Auction_won.objects.create(auction_won_by=user, item=item, amount=5000)

    response = client.delete('/online_auction/payment/1/')
    assert response.status_code == 405
    assert response.json() == {"message": "Invalid request method"}

