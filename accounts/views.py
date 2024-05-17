from rest_framework import status
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
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
        phone_number = data['phone_number']
        password = data['password']
        password2 = data['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                return Response({'error': 'Email already exists'})


            else:
                user = User.objects.create_user(email=email, password=password, name=name, phone_number=phone_number)
                user.save()
                return Response({'success': 'User created succesfully'})
        else:
            return Response({'error': 'The Passwords do not match'})


class LoginView(TokenObtainPairView):
    permission_classes = (permissions.AllowAny, )
    serializer_class = MyTokenObtainPairSerializer


class ProfileUpdateView(APIView):
    permission_classes = (permissions.IsAuthenticated, )
    parser_classes = [MultiPartParser, FormParser, JSONParser]

    def patch(self, request, *args, **kwargs):
        user = request.user
        serializer = UserAccountSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserListView(APIView):
    def get(self, request):
        # Retrieve all blogs from the database
        blogs = UserAccount.objects.all()

        # Serialize the queryset
        serializer = UserAccountSerializer(blogs, many=True)

        # Return the serialized data as a JSON response
        return Response(serializer.data)