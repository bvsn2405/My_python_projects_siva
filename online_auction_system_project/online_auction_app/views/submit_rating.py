import json

from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from ..models.Items import Items
from ..models.Ratings import Ratings
from ..models.auction_won import Auction_won
from ..models.payment import Payment


class SubmitRatingForItemBought(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def post(self, request, id):

        user = request.user
        try:
            item = Items.objects.get(id=id)
            print(item.title)
            try:
                auction = Auction_won.objects.get(item=item, auction_won_by=user)
                print(f"item price:{auction.amount}")

                try:
                    payment = Payment.objects.get(item=item, buyer=user)
                    print(payment.payment_done)
                    try:
                        data = json.loads(request.body)
                        review = data.get('review', '')
                        raw_rating = data.get('rating')

                        if raw_rating is not None:
                            rating = min(max(raw_rating, 0), 5)

                            try:
                                existing_rating = Ratings.objects.get(item=item, buyer=user)
                                print('Rating found')
                                existing_rating.rating = rating
                                existing_rating.review = review
                                existing_rating.save()
                                print('Rating updated')

                                return JsonResponse(
                                    {"message": "Rating and review for the product updated successfully!"})
                            except Ratings.DoesNotExist:
                                Ratings.objects.create(buyer=user, item=item, rating=rating, review=review)
                                return JsonResponse(
                                    {"message": "Rating and review for the product submitted successfully!"})
                        else:
                            return JsonResponse({"message": "Invalid rating provided"}, status=400)
                    except json.JSONDecodeError:
                        return JsonResponse({"message": "Invalid JSON data provided"}, status=400)
                except:
                    return JsonResponse({"message": "You have to make payment for the item before you rate it!!"},
                                        status=400)
            except:
                return JsonResponse({"message": "The Auction belongs to others!"}, status=400)
        except:
            return JsonResponse({"message": "The Auction does not exist!"}, status=400)
