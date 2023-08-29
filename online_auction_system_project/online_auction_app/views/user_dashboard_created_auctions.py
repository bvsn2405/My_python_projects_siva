from datetime import datetime,timezone

from django.contrib.auth.models import User
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from ..models.Items import Items


class UserDashboardCreatedAuctions(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, request):
        user = request.user

        items = Items.objects.filter(seller=user)
        time_now = datetime.now(timezone.utc)
        auction_data = []

        for item in items:
            auction = {
                "Action Id": item.id,
                "Auction ends in": str(item.auction_end_time - time_now),
                "Auction created by": user.username,
                "Starting Price": item.starting_price}
            auction_data.append(auction)

        return JsonResponse({f"Auctions created by {user.username}": auction_data})


    def post(self, request):
        return JsonResponse({"message": "Invalid request method"}, status=405)

    def put(self, request):
        return JsonResponse({"message": "Invalid request method"}, status=405)

    def patch(self, request):
        return JsonResponse({"message": "Invalid request method"}, status=405)

    def delete(self, request):
        return JsonResponse({"message": "Invalid request method"}, status=405)
