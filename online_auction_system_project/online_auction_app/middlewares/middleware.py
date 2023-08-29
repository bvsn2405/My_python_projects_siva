from django.http import JsonResponse


class CustomAuthenticationMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        paths = [
            "/online_auction/login/",
            "/online_auction/logout/",
            "/online_auction/user_reg/",
            "/online_auction/display_auctions/",
            "/online_auction/display_auctions/",
            "/online_auction/auctions_closed/",
            "/online_auction/update_auctions_status/"]

        if request.path in paths or request.path.startswith("/online_auction/auction/"):
            response = self.get_response(request)
            return response
        else:
            if not request.user.is_authenticated:
                return JsonResponse({"message": "User is not authenticated"}, status=400)

            response = self.get_response(request)
        return response
