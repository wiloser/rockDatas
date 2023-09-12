from django.shortcuts import render


class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if (request.path != '/loginn') and (request.path != '') and (request.path != '/register') and (request.path != '/admin'):
            try:
                if not request.user.is_authenticated:
                    return render(request, 'login.html')
            except:
                return render(request, 'login.html')
        return response

