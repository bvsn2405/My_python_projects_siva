import json
from online_auction_app.models.Bid import Bid
from datetime import datetime,timezone
import pytest
from rest_framework.test import APIClient

client = APIClient()


@pytest.mark.django_db(transaction=True)
def test_user_dashboard_participated_auctions_success(create_user_admin,create_item):
    client.post('/online_auction/login/', json.dumps({"username": "admin", "password": "admin"}),
                content_type='application/json')


    time_now = datetime.now()
    Bid.objects.create(
        user=create_user_admin,
        item=create_item,
        bid_amount=100,
        bid_time=time_now)

    response = client.get('/online_auction/dashboard/participated_auctions/')
    data = response.json()[f"Bids participated by {create_user_admin.username}"]

    assert response.status_code == 200
    assert len(data) == 1
    assert data[0]["Action Id"] == 1
    assert data[0]["Bid amount"] == 100


@pytest.mark.django_db(transaction=True)
def test_user_dashboard_participated_auctions_without_authorizing(create_user_admin):


    response = client.get('/online_auction/dashboard/participated_auctions/')

    assert response.status_code == 400
    assert response.json() == {"message": "User is not authenticated"}


@pytest.mark.django_db(transaction=True)
def test_user_dashboard_participated_auctions_invalid_request_method_post(create_user_admin):
    client.post('/online_auction/login/', json.dumps({"username": "admin", "password": "admin"}),
                content_type='application/json')

    response = client.post('/online_auction/dashboard/participated_auctions/')

    assert response.status_code == 405
    assert response.json() == {"message": "Invalid request method"}


@pytest.mark.django_db(transaction=True)
def test_user_dashboard_participated_auctions_invalid_request_method_put(create_user_admin):
    client.post('/online_auction/login/', json.dumps({"username": "admin", "password": "admin"}),
                content_type='application/json')

    response = client.put('/online_auction/dashboard/participated_auctions/')

    assert response.status_code == 405
    assert response.json() == {"message": "Invalid request method"}


@pytest.mark.django_db(transaction=True)
def test_user_dashboard_participated_auctions_invalid_request_method_patch(create_user_admin):
    client.post('/online_auction/login/', json.dumps({"username": "admin", "password": "admin"}),
                content_type='application/json')

    response = client.patch('/online_auction/dashboard/participated_auctions/')

    assert response.status_code == 405
    assert response.json() == {"message": "Invalid request method"}


@pytest.mark.django_db(transaction=True)
def test_user_dashboard_participated_auctions_invalid_request_method_delete(create_user_admin):
    client.post('/online_auction/login/', json.dumps({"username": "admin", "password": "admin"}),
                content_type='application/json')

    response = client.delete('/online_auction/dashboard/participated_auctions/')

    assert response.status_code == 405
    assert response.json() == {"message": "Invalid request method"}