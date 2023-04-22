# from rest_framework.decorators import api_view
from django.contrib.auth.models import User
# from proyectos.serializers.user import *

# import openpyxl

# from django.core.exceptions import ValidationError

# @api_view(['POST'])
# def register_users_from_excel(request):
#     file=request.data.get('file'),
#     # Cargar el archivo Excel usando openpyxl
#     workbook = openpyxl.load_workbook(file)
#     worksheet = workbook.active

#     # Recorrer cada fila del archivo Excel y crear un usuario para cada una
#     for row in worksheet.iter_rows(min_row=2):
#         username = row[0].value
#         # first_name = row[1].value
#         # last_name = row[2].value
#         email = row[1].value
#         password = row[2].value

#         # Crear el usuario
#         try:
#             user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email, password=password)
#             user.save()
#         except ValidationError as e:
#             # Manejar el caso de que la validación falle
#             print(f"Error al crear usuario {username}: {e.message}")
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from allauth.account.utils import complete_signup
from allauth.account import app_settings as allauth_settings
from allauth.utils import email_address_exists, get_username_max_length

@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    email = request.data.get('email', '')
    password = request.data.get('password', '')
    username = request.data.get('username', '')

    if email and password and username:
        if email_address_exists(email):
            return Response({'error': 'Email already exists'})
        user = User.objects.create_user(username=username, email=email, password=password)
        token, created = Token.objects.get_or_create(user=user)
        complete_signup(request, user, allauth_settings.EMAIL_VERIFICATION, None)
        return Response({'token': token.key})
    else:
        return Response({'error': 'Missing parameter'})