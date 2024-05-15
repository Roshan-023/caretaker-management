from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import *

User = get_user_model()

class SignUpView(APIView):
    permission_classes = (permissions.AllowAny, )

    def post(self, request, format=None):
        data = self.request.data

        name = data['name']
        email = data['email']
        password = data['password']
        password2 = data['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                return Response({'error': 'Email already exists'})


            else:
                user = User.objects.create_user(email=email, password=password, name=name)
                user.save()
                return Response({'success': 'User created succesfully'})


        else:
            return Response({'error': 'The Passwords do not match'})


class LoginView(TokenObtainPairView):
    permission_classes = (permissions.AllowAny, )
    serializer_class = MyTokenObtainPairSerializer