import json

from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from ..models.Items import Items
from ..models.auction_won import Auction_won
from ..models.payment import Payment


class payment_to_auction_won(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def post(self, request, auction_id):

        user = request.user
        try:
            item = Items.objects.get(id=auction_id)
            try:
                auction = Auction_won.objects.get(item=item, auction_won_by=user)

                try:
                    payment = Payment.objects.get(item=item)
                    return JsonResponse({"message": "Already payment done !"}, status=400)
                except:

                    data = json.loads(request.body)
                    try:
                        amount_received = data['amount']
                        if auction.amount == amount_received:
                            Payment.objects.create(
                                buyer=user,
                                item=item,
                                payment_done=True,
                                amount=amount_received)
                            return JsonResponse({"message": "Payment done successfully !"})
                        else:
                            return JsonResponse({"message": "Payment failed",
                                                 "error message": f"You have to pay: {auction.amount},but you paid: {amount_received}"},
                                                status=400)
                    except:
                        return JsonResponse({"message": "Invalid data provided !"}, status=400)
            except:
                return JsonResponse({"message": "The auction does not won by you! It belongs to others"}, status=400)
        except:
            return JsonResponse({"message": "The auction does not exists"}, status=400)

    def get(self, request, auction_id):
        return JsonResponse({"message": "Invalid request method"}, status=405)

    def put(self, request, auction_id):
        return JsonResponse({"message": "Invalid request method"}, status=405)

    def patch(self, request, auction_id):
        return JsonResponse({"message": "Invalid request method"}, status=405)

    def delete(self, request, auction_id):
        return JsonResponse({"message": "Invalid request method"}, status=405)
