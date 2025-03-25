from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import AccessToken
from .serializers import UserRegistrationSerializer
from django.contrib.auth.models import User

# Generate Access Token Function 
def get_access_token_for_user(user):
    access = AccessToken.for_user(user)
    return {
        'access': str(access),
    }

# User Registration View 
class UserRegistrationView(APIView):
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save() 
            return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# User Login View 
class UserLoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)
        if user:
            token = get_access_token_for_user(user)  
            return Response({"message": "Login successful", "token": token}, status=status.HTTP_200_OK)
        else:
            return Response({"message": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

# User Logout View 
class UserLogoutView(APIView):
    def post(self, request):
        return Response({"message": "Logout sucessfull"}, status=status.HTTP_200_OK)
