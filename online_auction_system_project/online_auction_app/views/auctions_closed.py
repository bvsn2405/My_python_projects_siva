from django.db.models import Max, F
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from ..models.Bid import Bid
from ..models.auction_won import Auction_won
from django.contrib.auth.models import User
from ..models.Items import Items


class AuctionsClosedView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, request):
        highest_bid_info = Bid.objects.filter(item__is_active=False).annotate(
            highest_bid=Max('bid_amount'),
            highest_bid_user=F('user')
        ).values('item', 'highest_bid', 'highest_bid_user')
        data_list = []
        for item_data in highest_bid_info:
            item_id = item_data['item']
            highest_bid_amount = item_data['highest_bid']
            highest_bid_user = item_data['highest_bid_user']
            user = User.objects.get(id=highest_bid_user)
            item = Items.objects.get(id=item_id)
            data = {
                "Auction ": item_id,
                "Item name ": item.title,
                "Highest bid amount ": highest_bid_amount,
                "Highest bid done by ": user.username
            }
            data_list.append(data)
            if not Auction_won.objects.filter(item=item).exists :
                Auction_won.objects.create(auction_won_by=user, item=item, amount=highest_bid_amount)



        return JsonResponse({"Completed Auctions details": data_list})

    def post(self, request):
        return JsonResponse({"message": "Invalid request method"}, status=405)

    def put(self, request):
        return JsonResponse({"message": "Invalid request method"}, status=405)

    def patch(self, request):
        return JsonResponse({"message": "Invalid request method"}, status=405)

    def delete(self, request):
        return JsonResponse({"message": "Invalid request method"}, status=405)
