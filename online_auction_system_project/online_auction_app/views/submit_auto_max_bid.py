import json
from datetime import datetime, timezone

from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from ..models.Automatic_Bid import Automatic_Bid
from ..models.Items import Items


class SubmitMaxBidView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def post(self, request, auction_id):
        try:
            data = json.loads(request.body)
            item_data = Items.objects.get(id=auction_id)
            max_bid_amount = data['max_bid_amount']
            bid_time = datetime.now(timezone.utc)
            user = request.user

            if bid_time > item_data.auction_end_time:
                return JsonResponse({"message": "Auction is closed. It is not active"}, status=400)

            if not Automatic_Bid.objects.filter(item=item_data,user=request.user).exists():
                if item_data.starting_price > max_bid_amount:
                    return JsonResponse({"message": "The bid amount should be more than the starting price",
                                         "The starting price for this item is": item_data.starting_price},
                                        status=400)
                else:
                    Automatic_Bid.objects.create(user=user, item=item_data, bid_time=bid_time,
                                                 max_bid_amount=max_bid_amount)
                    return JsonResponse({"message": "Bid submitted successfully"})
            else:
                return JsonResponse({"message": "You already submitted the bid for this item!"}, status=400)

        except Items.DoesNotExist:
            return JsonResponse({"message": "The auction does not exist"}, status=400)

        except Exception as e:
            return JsonResponse({"Error message": "Invalid data submitted"}, status=400)

    def get(self, request,auction_id):
        return JsonResponse({"message": "Invalid request method"}, status=405)

    def put(self, request,auction_id):
        return JsonResponse({"message": "Invalid request method"}, status=405)

    def patch(self, request,auction_id):
        return JsonResponse({"message": "Invalid request method"}, status=405)

    def delete(self, request,auction_id):
        return JsonResponse({"message": "Invalid request method"}, status=405)
