import json
import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from online_auction_app.models.Items import Items
from datetime import datetime,timedelta

client = APIClient()


@pytest.fixture()
def create_user():
    return User.objects.create_user(username="admin", password="admin", email="siva.bvsn@gmail.com")


@pytest.mark.django_db(transaction=True)
def test_submit_auction(create_user):
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
    response = client.post('/online_auction/submit_bid/1/', json.dumps(data), content_type='application/json')
    assert response.status_code == 200


@pytest.mark.django_db(transaction=True)
def test_submit_auction_invalid_data(create_user):
    client.post('/online_auction/login/', data=json.dumps({"username": "admin", "password": "admin"}),
                content_type='application/json')
    data = {
        'title': 'Test Auction',
        'description': 'Test description',
        'image': "F:\\car-lamborghini-revuelto-127-641a1d518802b.jpg",
        'starting_price': 100,
        'no_of_days_auction_ends': 0,
    }

    data = {"bid_amount1": 1000}
    response = client.post('/online_auction/submit_bid/1/', json.dumps(data), content_type='application/json')
    assert response.status_code == 400


@pytest.mark.django_db(transaction=True)
def test_submit_auction_closed_auction(create_user_admin):
    client.post('/online_auction/login/', data=json.dumps({"username": "admin", "password": "admin"}),
                content_type='application/json')
    time_now = datetime.now() - timedelta(2)
    Items.objects.create(
        title='Title',
        description='Description',
        image="siva.jpg",
        starting_price=100,
        seller=create_user_admin,
        auction_end_time=time_now,
        is_active=False)
    data = {"bid_amount": 1000}
    response = client.post('/online_auction/submit_bid/1/', json.dumps(data), content_type='application/json')
    assert response.status_code == 400


@pytest.mark.django_db(transaction=True)
def test_submit_auction_invalid_bid_amount(create_user):
    client.post('/online_auction/login/', data=json.dumps({"username": "admin", "password": "admin"}),
                content_type='application/json')
    data = {
        'title': 'Test Auction',
        'description': 'Test description',
        'image': "F:\\car-lamborghini-revuelto-127-641a1d518802b.jpg",
        'starting_price': 10000,
        'no_of_days_auction_ends': 0,
    }
    client.post('/online_auction/create_auction/', data, format='multipart')
    data = {"bid_amount": 1000}
    response = client.post('/online_auction/submit_bid/1/', json.dumps(data), content_type='application/json')
    assert response.status_code == 400


@pytest.mark.django_db(transaction=True)
def test_submit_auction_invalid_bid_amount_1(create_user):
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
    response = client.post('/online_auction/submit_bid/1/', json.dumps(data), content_type='application/json')
    data = {"bid_amount": 500}
    response = client.post('/online_auction/submit_bid/1/', json.dumps(data), content_type='application/json')
    assert response.status_code == 400

@pytest.mark.django_db
def test_submit_bid_invalid_request_method_get(create_user):
    client.post('/online_auction/login/', data=json.dumps({"username": "admin", "password": "admin"}),
                content_type='application/json')
    payload = json.dumps({})
    response = client.get('/online_auction/submit_bid/1/')
    assert response.status_code == 405
    assert response.json() == {"message": "Invalid request method"}


@pytest.mark.django_db
def test_submit_bid_invalid_request_method_put(create_user):
    client.post('/online_auction/login/', data=json.dumps({"username": "admin", "password": "admin"}),
                content_type='application/json')
    payload = json.dumps({})
    response = client.put('/online_auction/submit_bid/1/', payload, content_type='application/json')
    assert response.status_code == 405
    assert response.json() == {"message": "Invalid request method"}


@pytest.mark.django_db
def test_submit_bid_invalid_request_method_patch(create_user):
    client.post('/online_auction/login/', data=json.dumps({"username": "admin", "password": "admin"}),
                content_type='application/json')
    payload = json.dumps({})
    response = client.patch('/online_auction/submit_bid/1/', payload, content_type='application/json')
    assert response.status_code == 405
    assert response.json() == {"message": "Invalid request method"}


@pytest.mark.django_db
def test_submit_bid_invalid_request_method_delete(create_user):
    client.post('/online_auction/login/', data=json.dumps({"username": "admin", "password": "admin"}),
                content_type='application/json')
    payload = json.dumps({})
    response = client.delete('/online_auction/submit_bid/1/')
    assert response.status_code == 405
    assert response.json() == {"message": "Invalid request method"}
