from datetime import datetime,timezone,timedelta

from django.contrib.auth.models import User
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from ..models.Items import Items


class DisplayAuctionsView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, request):

        items = Items.objects.filter(is_active=True)
        time_now = datetime.now(timezone.utc)
        auction_data = []

        for item in items:
            auction = {
                "Action Id": item.id,
                "Auction ends in": str(item.auction_end_time - time_now),
                "Auction created by": item.seller.username,
                "Starting Price": item.starting_price}
            auction_data.append(auction)

        return JsonResponse({"Auctions in active state": auction_data})

    def post(self, request):
        return JsonResponse({"message": "Invalid request method"}, status=405)

    def put(self, request):
        return JsonResponse({"message": "Invalid request method"}, status=405)

    def patch(self, request):
        return JsonResponse({"message": "Invalid request method"}, status=405)

    def delete(self, request):
        return JsonResponse({"message": "Invalid request method"}, status=405)
