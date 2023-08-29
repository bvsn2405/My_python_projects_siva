from django.urls import path

from .views.auctions_closed import AuctionsClosedView
from .views.create_auction import CreateAuctionView
from .views.display_all_actions import DisplayAuctionsView
from .views.login import LoginView
from .views.logout import LogoutView
from .views.submit_bid import SubmitBidView
from .views.update_inactive_actions import update_auction_status
from .views.user_dashboard_created_auctions import UserDashboardCreatedAuctions
from .views.user_registration import UserRegistrationView
from .views.user_dashboard_auctions_participated import UserDashboardParticipatedAuctions
from .views.user_dashboard_auctions_won import UserDashboardAuctionsWon
from .views.display_auction_by_id import DisplayAuctionByIdView
from .views.submit_auto_max_bid import SubmitMaxBidView
from .views.payment_to_auction_won import payment_to_auction_won
from .views.submit_rating import SubmitRatingForItemBought

urlpatterns = [
    path('user_reg/', UserRegistrationView.as_view(), name='user_reg'),
    path('create_auction/', CreateAuctionView.as_view(), name='create_auction'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('display_auctions/', DisplayAuctionsView.as_view(), name='display_auctions'),
    path('submit_bid/<int:auction_id>/', SubmitBidView.as_view(), name='submit_bid'),
    path('update_auctions_status/', update_auction_status, name='update_auctions_status'),
    path('auctions_closed/', AuctionsClosedView.as_view(), name='auctions_closed'),
    path('dashboard/created_auctions/', UserDashboardCreatedAuctions.as_view(), name='dashboard_created_auctions'),
    path('dashboard/participated_auctions/', UserDashboardParticipatedAuctions.as_view(),
         name='dashboard_participated_auctions'),
    path('dashboard/auctions_won/', UserDashboardAuctionsWon.as_view(),
         name='dashboard_auctions_won'),
    path('auction/<int:id>/', DisplayAuctionByIdView.as_view(), name='display_auction'),
    path('submit_max_bid/<int:auction_id>/', SubmitMaxBidView.as_view(), name='submit_max_bid'),
    path('payment/<int:auction_id>/', payment_to_auction_won.as_view(), name='payment'),
    path('submit_rating/<int:id>/', SubmitRatingForItemBought.as_view(), name='rating'),

]
