from django.contrib.auth import logout
from django.shortcuts import redirect
from rest_framework.authtoken.models import Token

def logout_view(request):
    Token.objects.filter(user=request.user).delete()
    logout(request)
    return redirect('/')
