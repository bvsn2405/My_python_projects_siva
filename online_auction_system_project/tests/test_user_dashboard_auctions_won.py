import json

import pytest
from rest_framework.test import APIClient

client = APIClient()


@pytest.mark.django_db(transaction=True)
def test_user_dashboard_auctions_won_success(create_user_admin,create_auction_won):
    client.post('/online_auction/login/', json.dumps({"username": "admin", "password": "admin"}),
                content_type='application/json')

    response = client.get('/online_auction/dashboard/auctions_won/')
    auctions = response.json()[f"Auctions won by {create_user_admin.username}"]

    assert response.status_code == 200
    assert auctions == [{
            "Action Id": 1,
            "Amount": 100
        }]


@pytest.mark.django_db(transaction=True)
def test_user_dashboard_auctions_won_without_authorizing(create_user_admin):

    data = {
        'title': 'Test Auction',
        'description': 'Test description',
        'image': "F:\\car-lamborghini-revuelto-127-641a1d518802b.jpg",
        'starting_price': 100,
        'no_of_days_auction_ends': 3,
    }
    client.post('/online_auction/create_auction/', data, format='multipart')
    response = client.get('/online_auction/dashboard/auctions_won/')

    assert response.status_code == 400
    assert response.json() == {"message": "User is not authenticated"}


@pytest.mark.django_db(transaction=True)
def test_user_dashboard_auctions_won_invalid_request_method_post(create_user_admin):
    client.post('/online_auction/login/', json.dumps({"username": "admin", "password": "admin"}),
                content_type='application/json')

    response = client.post('/online_auction/dashboard/auctions_won/')

    assert response.status_code == 405
    assert response.json() == {"message": "Invalid request method"}


@pytest.mark.django_db(transaction=True)
def test_user_dashboard_auctions_won_invalid_request_method_put(create_user_admin):
    client.post('/online_auction/login/', json.dumps({"username": "admin", "password": "admin"}),
                content_type='application/json')

    response = client.put('/online_auction/dashboard/auctions_won/')

    assert response.status_code == 405
    assert response.json() == {"message": "Invalid request method"}


@pytest.mark.django_db(transaction=True)
def test_user_dashboard_auctions_won_invalid_request_method_patch(create_user_admin):
    client.post('/online_auction/login/', json.dumps({"username": "admin", "password": "admin"}),
                content_type='application/json')

    response = client.patch('/online_auction/dashboard/auctions_won/')

    assert response.status_code == 405
    assert response.json() == {"message": "Invalid request method"}


@pytest.mark.django_db(transaction=True)
def test_user_dashboard_auctions_won_invalid_request_method_delete(create_user_admin):
    client.post('/online_auction/login/', json.dumps({"username": "admin", "password": "admin"}),
                content_type='application/json')

    response = client.delete('/online_auction/dashboard/auctions_won/')

    assert response.status_code == 405
    assert response.json() == {"message": "Invalid request method"}