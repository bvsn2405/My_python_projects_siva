from django.contrib.auth import logout
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

class LogoutView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, request):

        if request.user.is_authenticated:
            logout(request)
            return JsonResponse({'message': 'Logged out successfully'})
        else:
            return JsonResponse({'message': 'Already logged out'}, status=400)

    def post(self, request):
        return JsonResponse({"message": "Invalid request method"}, status=405)

    def put(self, request):
        return JsonResponse({"message": "Invalid request method"}, status=405)

    def patch(self, request):
        return JsonResponse({"message": "Invalid request method"}, status=405)

    def delete(self, request):
        return JsonResponse({"message": "Invalid request method"}, status=405)
