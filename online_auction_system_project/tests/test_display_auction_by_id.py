import json

import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from datetime import datetime,timedelta
from online_auction_app.models.Items import Items
from online_auction_app.models.auction_won import Auction_won
from online_auction_app.models.Bid import Bid
from online_auction_app.models.Automatic_Bid import Automatic_Bid




client = APIClient()


@pytest.fixture()
def create_user():
    return User.objects.create_user(username="admin", password="admin", email="siva.bvsn@gmail.com")


@pytest.mark.django_db(transaction=True)
def test_display_auction_by_id_success(create_user):
    client.post('/online_auction/login/', data=json.dumps({"username": "admin", "password": "admin"}),
                content_type='application/json')
    data = {
        'title': 'Test Auction',
        'description': 'Test description',
        'image': "F:\\car-lamborghini-revuelto-127-641a1d518802b.jpg",
        'starting_price': 100,
        'no_of_days_auction_ends': 0,
    }
    client.post('/online_auction/create_auction/', data, format='multipart')
    data = {"bid_amount": 1000}
    client.post('/online_auction/submit_bid/1/', json.dumps(data), content_type='application/json')
    data = {"bid_amount": 1000}
    client.post('/online_auction/submit_bid/1/', json.dumps(data), content_type='application/json')

    response = client.get('/online_auction/auction/1/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_display_auction_by_id_invalid_request_method_post():
    response = client.post('/online_auction/auction/1/')
    assert response.status_code == 405
    assert response.json() == {"message": "Invalid request method"}


@pytest.mark.django_db
def test_display_auction_by_id_invalid_request_method_put():

    response = client.put('/online_auction/auction/1/')
    assert response.status_code == 405
    assert response.json() == {"message": "Invalid request method"}


@pytest.mark.django_db
def test_display_auction_by_id_invalid_request_method_patch():

    response = client.patch('/online_auction/auction/1/')
    assert response.status_code == 405
    assert response.json() == {"message": "Invalid request method"}


@pytest.mark.django_db
def test_display_auction_by_id_invalid_request_method_delete():

    response = client.delete('/online_auction/auction/1/')
    assert response.status_code == 405
    assert response.json() == {"message": "Invalid request method"}



@pytest.mark.django_db
def test_display_auction_by_id_auction_does_not_exist():
    response = client.get('/online_auction/auction/111/')
    assert response.status_code == 400
    assert response.json() == {"message": "The auction does not exist !"}


@pytest.mark.django_db
def test_display_auction_by_id_2(create_user_admin):

    user1 = User.objects.create_user(username='admin1', password='admin1', email='admin@gmail.com')
    user2 = User.objects.create_user(username='admin2', password='admin2', email='admin@gmail.com')


    time_now = datetime.now()
    item1 = Items.objects.create(title='Title', description='Description', image="siva.jpg",
                                 starting_price=100, seller=create_user_admin, auction_end_time=time_now+timedelta(1),
                                 is_active=True)
    item2 = Items.objects.create(title='Title', description='Description', image="siva.jpg",
                                 starting_price=100, seller=create_user_admin, auction_end_time=time_now,
                                 is_active=True)

    Bid.objects.create(user=user1, item=item1, bid_amount=1000, bid_time=time_now)
    Bid.objects.create(user=user2, item=item1, bid_amount=1100, bid_time=time_now)

    Bid.objects.create(user=user1, item=item2, bid_amount=1000, bid_time=time_now)
    Bid.objects.create(user=user2, item=item2, bid_amount=1100, bid_time=time_now)

    item2.auction_end_time = time_now - timedelta(1)
    item2.save()

    client.get('/online_auction/update_auctions_status/')

    response = client.get('/online_auction/auction/1/')
    assert response.status_code == 200
    response = client.get('/online_auction/auction/1/')
    assert response.status_code == 200



@pytest.mark.django_db
def test_display_auction_by_id_3(create_user_admin):

    time_now = datetime.now()
    item1 = Items.objects.create(title='Title', description='Description', image="siva.jpg",
                                 starting_price=100, seller=create_user_admin, auction_end_time=time_now+timedelta(1),
                                 is_active=True)
    item2 = Items.objects.create(title='Title', description='Description', image="siva.jpg",
                                 starting_price=100, seller=create_user_admin, auction_end_time=time_now,
                                 is_active=True)

    item2.auction_end_time = time_now - timedelta(1)
    item2.save()

    client.get('/online_auction/update_auctions_status/')

    response = client.get('/online_auction/auction/1/')
    assert response.status_code == 200
    response = client.get('/online_auction/auction/2/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_display_auction_by_id_2(create_user_admin):

    user1 = User.objects.create_user(username='admin1', password='admin1', email='admin@gmail.com')
    user2 = User.objects.create_user(username='admin2', password='admin2', email='admin@gmail.com')


    time_now = datetime.now()
    item2 = Items.objects.create(title='Title', description='Description', image="siva.jpg",
                                 starting_price=100, seller=create_user_admin, auction_end_time=time_now+timedelta(1),
                                 is_active=True)
    item1 = Items.objects.create(title='Title', description='Description', image="siva.jpg",
                                 starting_price=100, seller=create_user_admin, auction_end_time=time_now - timedelta(1),
                                 is_active=True)

    Bid.objects.create(user=user1, item=item1, bid_amount=1000, bid_time=time_now)
    Bid.objects.create(user=user2, item=item1, bid_amount=1100, bid_time=time_now)


    item1.auction_end_time = time_now - timedelta(1)
    item1.save()

    client.get('/online_auction/update_auctions_status/')

    Auction_won.objects.create(
        auction_won_by=user1,
        item=item2,
        amount=10000)
    Auction_won.objects.create(
        auction_won_by=user1,
        item=item2,
        amount=10000)

    response = client.get('/online_auction/auction/1/')
    assert response.status_code == 200
    response = client.get('/online_auction/auction/2/')
    assert response.status_code == 200

