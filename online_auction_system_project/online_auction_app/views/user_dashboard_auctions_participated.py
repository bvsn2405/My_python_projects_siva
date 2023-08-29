from datetime import datetime,timezone

from django.contrib.auth.models import User
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from ..models.Items import Items
from ..models.Bid import Bid


class UserDashboardParticipatedAuctions(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, request):

        user = request.user
        bids = Bid.objects.filter(user=user)
        bids_data = []

        for bid in bids:

            bid_data = {
                "Action Id": bid.item_id,
                "Make bid on": bid.bid_time,
                "Bid amount": bid.bid_amount}
            bids_data.append(bid_data)

        return JsonResponse({f"Bids participated by {user.username}": bids_data})

    def post(self, request):
        return JsonResponse({"message": "Invalid request method"}, status=405)

    def put(self, request):
        return JsonResponse({"message": "Invalid request method"}, status=405)

    def patch(self, request):
        return JsonResponse({"message": "Invalid request method"}, status=405)

    def delete(self, request):
        return JsonResponse({"message": "Invalid request method"}, status=405)
