from datetime import datetime, timezone
from datetime import timedelta

from django.conf import settings
from django.contrib.auth.models import User
from django.db.models import Max, F, Min
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from ..models.Bid import Bid
from ..models.Items import Items
from ..models.auction_won import Auction_won


class DisplayAuctionByIdView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, request, id):

        try:
            item = Items.objects.get(id=id)
            image_url = f"{settings.MEDIA_URL}{item.image}"

            time_now = datetime.now(timezone.utc)
            user=item.seller
            if item.auction_end_time < time_now :
                auction_ends = "Auction already closed"
            else:
                auction_ends = str(item.auction_end_time - time_now)


            if item.is_active:
                highest_bid_info = Bid.objects.filter(item_id=item.id).values('item').annotate(
                    highest_bid=Max('bid_amount'),
                    earliest_bid_time=Min('bid_time'),
                    highest_bid_user=F('user')
                ).filter(highest_bid=F('bid_amount'), bid_time=F('earliest_bid_time')).order_by('item', '-highest_bid',
                                                                                                'earliest_bid_time').first()
                if highest_bid_info is not None:
                    auction_status = 'Auction is not closed '
                    max_bid = highest_bid_info['highest_bid']

                    user_id = highest_bid_info['highest_bid_user']
                    max_bid_by = User.objects.get(id=user_id).username
                else:
                    auction_status = 'Auction is not closed '
                    max_bid = None
                    max_bid_by = None


            else:
                try:
                    auction_won = Auction_won.objects.filter(item=item).first()
                    auction_status = 'Auction closed and won by'
                    max_bid = auction_won.amount
                    max_bid_by = User.objects.get(id=auction_won.auction_won_by_id).username
                except:

                    auction_status = 'Auction closed no one participated in the bid'
                    max_bid = None
                    max_bid_by = None

            auction = {
                "Action Id": item.id,
                "Auction ends in": auction_ends,
                "Auction created by": user.username,
                "Starting Price": item.starting_price,
                "Auction status": auction_status,
                "Maximum bid amount": max_bid,
                "Maximum bid done by/won by": max_bid_by,
                "Auction item image url ": image_url
            }

            return JsonResponse({"Auctions Details": auction})

        except :
            return JsonResponse({"message": "The auction does not exist !"}, status=400)

    def post(self, request, id):
        return JsonResponse({"message": "Invalid request method"}, status=405)

    def put(self, request, id):
        return JsonResponse({"message": "Invalid request method"}, status=405)

    def patch(self, request, id):
        return JsonResponse({"message": "Invalid request method"}, status=405)

    def delete(self, request, id):
        return JsonResponse({"message": "Invalid request method"}, status=405)
