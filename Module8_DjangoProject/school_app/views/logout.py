from django.contrib.auth import logout
from django.http import JsonResponse

def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        return JsonResponse({'message': 'Logged out successfully'})
    else:
        return JsonResponse({'message': 'Already logged out'})
