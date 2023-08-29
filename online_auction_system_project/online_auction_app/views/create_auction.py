from datetime import datetime, timedelta
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from ..models.Items import Items


class CreateAuctionView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def post(self, request):

        user = request.user

        required_params = ['title', 'description', 'image', 'starting_price', 'no_of_days_auction_ends']
        errors = []
        for param in required_params:
            if param not in request.POST and param not in request.FILES:
                errors.append(param)
        if errors:
            return JsonResponse({'message': f'Missing required parameters: {errors}'}, status=400)

        title = request.POST.get('title')
        description = request.POST.get('description')
        image = request.FILES.get('image')
        starting_price = request.POST.get('starting_price')
        no_of_days_auction_ends = float(request.POST.get('no_of_days_auction_ends'))
        end_time = datetime.now() + timedelta(days=no_of_days_auction_ends)

        Items.objects.create(
            title=title, description=description, image=image, starting_price=starting_price, seller=user,
            auction_end_time=end_time, is_active=True)
        return JsonResponse({"message": "Auction created successfully !"})

    def get(self, request):
        return JsonResponse({"message": "Invalid request method"}, status=405)

    def put(self, request):
        return JsonResponse({"message": "Invalid request method"}, status=405)

    def patch(self, request):
        return JsonResponse({"message": "Invalid request method"}, status=405)

    def delete(self, request):
        return JsonResponse({"message": "Invalid request method"}, status=405)
