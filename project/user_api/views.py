from rest_framework.views import APIView
from django.contrib.auth import get_user_model, login, logout
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import SessionAuthentication
from rest_framework import permissions, status
from .serializers import User, UserRegisterSerializer, UserLoginSerializer, UserSerializer
from .validation import custom_validation, validate_email, validate_password


class UserRegister(APIView):
    permission_classes = (permissions.AllowAny)

    def post(self, request):
        clean_data = custom_validation(request.data)
        serializer = UserRegisterSerializer(data=clean_data)

        if serializer.is_valid(raise_exception=True):
            user = serializer.create(clean_data)
            if user:
                return Response(status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class UserLogin(APIView):
    permission_classes = (permissions.AllowAny)
    authentication_classes = (SessionAuthentication)

    def post (self, request):
        data = request.data
        assert validate_email(data['email']) != None, 'Email is not valid'
        assert validate_password(data['password']) != None, 'Password is not valid'
        serializer = UserLoginSerializer(data=data)

        if serializer.is_valid(raise_exception=True):
            user = serializer.validate(data)
            login(request, user)
            return Response(serializer.data, status=status.HTTP_200_OK)
    
class UserLogout(APIView):
    def get(self, request):
        logout(request)
        return Response(status=status.HTTP_200_OK)

class UserView(APIView):
    permission_classes = (permissions.IsAuthenticated)
    authentication_classes = (SessionAuthentication)
    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response({'user': serializer.data}, status=status.HTTP_200_OK)