
#Django
from django.contrib.auth import authenticate
#django REST Framework
from rest_framework import serializers
from rest_framework.authtoken.models import Token

class UserLoginSerializer(serializers.Serializer):
    #User login serializer
    #Handle the  login request data
    email = serializers.EmailField()
    password = serializers.CharField(min_length=8,max_length=64)

    def validate(self, data):
        #verificar credenciales
        user = authentica(username=data['email'],password=data['password'])
        if not user:
            raise serializers.validationError('invalido las credenciales')
        self.context['user']=user
        return data
    
    def create (self,data):
        #Genetate or retrieve new token
        token, created = Token.objects.get_or_create(user=self.context['user'])
        return self.context['user'], token.key



# class UserLoginSerializer(serializers.Serializer):
#     email = serializers.EmailField()
#     password = serializers.CharField(write_only=True)

#     def validate(self, data):
#         email = data.get('email')
#         password = data.get('password')

#         if email and password:
#             user = authenticate(email=email, password=password)
#             if user:
#                 data['user'] = user
#             else:
#                 raise serializers.ValidationError("Unable to log in with provided credentials.")
#         else:
#             raise serializers.ValidationError("Must include 'email' and 'password'.")
#         return data
