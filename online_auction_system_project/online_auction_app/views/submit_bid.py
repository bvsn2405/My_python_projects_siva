import json
from datetime import datetime, timezone

from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from ..models.Bid import Bid
from ..models.Items import Items


class SubmitBidView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def post(self, request, auction_id):
        try:
            data = json.loads(request.body)

            item_data = Items.objects.get(id=auction_id)
            bid_amount = data['bid_amount']
            bid_time = datetime.now(timezone.utc)
            user = request.user


            if bid_time > item_data.auction_end_time:
                return JsonResponse({"message": "Auction is closed .It is not active"}, status=400)

            try:

                latest_bid = Bid.objects.filter(user_id=user.id, item=item_data).latest('bid_time')

                if latest_bid.bid_amount > bid_amount:

                    return JsonResponse({"message": "The bid amount should me more than the last bid",
                                         "Last bid amount for this item is ": latest_bid.bid_amount}, status=400)
                else:
                    Bid.objects.create(user=user, item=item_data, bid_time=bid_time, bid_amount=bid_amount)
                    return JsonResponse({"message": "Bid submitted successfully"})

            except:
                if item_data.starting_price > bid_amount:
                    return JsonResponse({"message": "The bid amount should me more than the starting price",
                                         "The starting price for this item is ": item_data.starting_price}, status=400)
                else:
                    Bid.objects.create(user=user, item=item_data, bid_time=bid_time, bid_amount=bid_amount)
                    return JsonResponse({"message": "Bid submitted successfully"})

        except:
            return JsonResponse({"Error message": "Invalid data submitted"}, status=400)

    def get(self, request, auction_id):
        return JsonResponse({"message": "Invalid request method"}, status=405)

    def put(self, request, auction_id):
        return JsonResponse({"message": "Invalid request method"}, status=405)

    def patch(self, request, auction_id):
        return JsonResponse({"message": "Invalid request method"}, status=405)

    def delete(self, request, auction_id):
        return JsonResponse({"message": "Invalid request method"}, status=405)
