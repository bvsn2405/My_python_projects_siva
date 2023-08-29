import pytest
from django.core.management import call_command
from django.contrib.auth.models import User
from online_auction_app.models.Items import Items
from online_auction_app.models.auction_won import Auction_won
from online_auction_app.models.Bid import Bid
from online_auction_app.models.Automatic_Bid import Automatic_Bid
from online_auction_app.models.payment import  Payment

from datetime import datetime


@pytest.fixture(autouse=True)
def enable_db_reset():
    """
    Custom fixture to reset the database before each test.
    """
    call_command('flush', interactive=False, verbosity=0)


@pytest.fixture()
def create_user_admin():
    user = User.objects.create_user(username='admin',password='admin',email='siva@gmail.com')
    return user


@pytest.fixture()
def create_item(create_user_admin):
    time_now = datetime.now()
    item = Items.objects.create(
        title='Title',
        description='Description',
        image="siva.jpg",
        starting_price=100,
        seller=create_user_admin,
        auction_end_time=time_now,
        is_active=True)
    return item


@pytest.fixture()
def create_bid(create_item,create_user_admin):
    time_now = datetime.now()
    bid = Bid.objects.create(
            user=create_user_admin,
            item=create_item,
            bid_amount=100,
            bid_time=time_now)

    return bid



@pytest.fixture()
def create_auto_bid(create_item):
    user = User.objects.create_user(username='siva',password='siva')
    time_now = datetime.now()
    auto_bid = Automatic_Bid.objects.create(
            user=user,
            item=create_item,
            max_bid_amount=1000,
            bid_time=time_now)

    return auto_bid


@pytest.fixture()
def create_auction_won(create_item,create_user_admin):
    auction_won = Auction_won.objects.create(
            auction_won_by=create_user_admin,
            item=create_item,
            amount=100)

    return auction_won


@pytest.fixture()
def create_payment(create_item,create_user_admin):
    payment = Payment.objects.create(
            buyer=create_user_admin,
            item=create_item,
            payment_done=True,
            amount=1000)

    return payment


