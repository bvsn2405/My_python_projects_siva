from datetime import timezone, datetime

from django.db.models import Max, F
from django.http import JsonResponse

from ..models.Bid import Bid
from ..models.Items import Items
from ..models.Automatic_Bid import Automatic_Bid
from ..models.auction_won import Auction_won


def update_auction_status(request):
    if request.method == "GET":
        items = Items.objects.filter(is_active=True)
        date_time_now = datetime.now(timezone.utc)

        for item in items:
            if item.auction_end_time <= date_time_now:
                item.is_active = False
                item.save()

        items = Items.objects.filter(is_active=False)
        bid_info = []

        for item in items:
            max_bid_info = Bid.objects.filter(item=item).aggregate(max_bid=Max('bid_amount'))
            max_bid_amount = max_bid_info['max_bid']

            max_bid_info2 = Automatic_Bid.objects.filter(item=item).aggregate(max_bid_auto=Max('max_bid_amount'))
            max_bid_amount2 = max_bid_info2['max_bid_auto']

            if max_bid_amount2 is not None:
                max_bid = max(max_bid_amount, max_bid_amount2)
            else:
                max_bid = max_bid_amount

            if max_bid is not None:
                if max_bid == max_bid_amount:
                    max_bid_obj = Bid.objects.filter(item=item, bid_amount=max_bid).first()
                    max_bid_user = max_bid_obj.user
                else:
                    max_bid_obj2 = Automatic_Bid.objects.filter(item=item, max_bid_amount=max_bid).first()
                    max_bid_user = max_bid_obj2.user

                auction_won_entry = Auction_won.objects.filter(item=item)
                if not auction_won_entry.exists():
                    auction_won = Auction_won.objects.create(
                        auction_won_by=max_bid_user,
                        item=item,
                        amount=max_bid
                    )
                    bid_info.append({
                        'item_id': item.id,
                        'max_bid_amount': max_bid,
                        'max_bid_user': max_bid_user.username,
                        'auction_won_entry_created': True
                    })
                else:
                    bid_info.append({
                        'item_id': item.id,
                        'max_bid_amount': max_bid,
                        'max_bid_user': max_bid_user.username,
                        'auction_won_entry_created': False
                    })
            else:
                bid_info.append({
                    'item_id': item.id,
                    'max_bid_amount': None,
                    'max_bid_user': "no one participated in auction",
                    'auction_won_entry_created': False
                })

        return JsonResponse({"message": "auction status updated successfully", "bid_info": bid_info})

    else:
        return JsonResponse({"message": "Invalid request method"}, status=405)