from django.http import JsonResponse

class CustomAuthenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
    
        if request.path ==  '/api/logout/' or request.path ==  '/api/login/' or request.path.startswith('/api/students/'):
            #print("middleware executing for login,logout,registraion")
            #print(request.path)
            response = self.get_response(request)
            return response
        else:
            if not request.user.is_authenticated:
                #print("middleware executing for other than login,logout,registraion")
                return JsonResponse({"message": "User is not authenticated"})

            response = self.get_response(request)
        #print("Both conditions are failed")
        return response
