from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from ..models.auction_won import Auction_won


class UserDashboardAuctionsWon(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, request):

        user = request.user
        auctions_won = Auction_won.objects.filter(auction_won_by=user)
        auction_data = []

        for auction_won in auctions_won:
            auction = {
                "Action Id": auction_won.item_id,
                "Amount": auction_won.amount}
            auction_data.append(auction)

        return JsonResponse({f"Auctions won by {user.username}": auction_data})


    def post(self, request):
        return JsonResponse({"message": "Invalid request method"}, status=405)

    def put(self, request):
        return JsonResponse({"message": "Invalid request method"}, status=405)

    def patch(self, request):
        return JsonResponse({"message": "Invalid request method"}, status=405)

    def delete(self, request):
        return JsonResponse({"message": "Invalid request method"}, status=405)
