from django.shortcuts import render
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from django.contrib.auth import login
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
# Create your views here.


class LoginAPI(APIView):
    def post(self, request):
        # Retrieve username and password from the request data
        username = request.data.get('username')
        password = request.data.get('password')

        # Authenticate the user
        user = authenticate(username=username, password=password)
        

        if user is not None:
            # Generate JWT tokens
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)

            # Return the tokens in the response
            return Response({
                'access_token': access_token,
                'refresh_token': str(refresh),
                'user_id': user.id,
                
            }, status=status.HTTP_200_OK)
        else:
            # Authentication failed, return appropriate response
            return Response({'error': 'Invalid username or password'}, status=status.HTTP_401_UNAUTHORIZED)