from django.http import JsonResponse

def requires_authorization(view_func):
    def wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return JsonResponse({"message": "User is not authorized"}, status=401)
        return view_func(request, *args, **kwargs)
    return wrapped_view
