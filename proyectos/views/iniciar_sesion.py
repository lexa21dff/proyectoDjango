# from rest_framework.authtoken.models import Token
# from rest_framework.decorators import api_view, permission_classes
# from rest_framework.permissions import AllowAny
# from rest_framework.response import Response
# from allauth.account.utils import complete_signup
# from allauth.account import app_settings as allauth_settings
# from allauth.utils import email_address_exists, get_username_max_length
# from django.contrib.auth.models import User
# from django.contrib.auth import authenticate, login, logout

# @api_view(['POST'])
# @permission_classes([AllowAny])
# def login(request):
#     email = request.data.get('email', '')
#     password = request.data.get('password', '')

#     if email and password:
#         user = authenticate(request=request, email=email, password=password)
#         if user is not None:
#             token, created = Token.objects.get_or_create(user=user)
#             return Response({'token': token.key})
#         else:
#             return Response({'error': 'Invalid credentials'})
#     else:
#         return Response({'error': 'Missing parameter'})


#Users views

# Django REST FRAMEWORK


from rest_framework.views import APIView
from rest_framework import status
#serializer
from proyectos.serializers.login import *

class UserLoginAPIView(APIView):
    def post(self, request, *args, **kwargs):
        #Hadlle HTTP POST    request.
        serializer =  UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user, token = serializer.save()
        data = {
            'user': 'ok',
            'token': token
        }
        return Response(data, status=status.HTTP_201_CREATED)
