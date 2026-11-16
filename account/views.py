
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from core.custom_throttle import LoginRateThrottle, RegisterRateThrottle

from .serializers import *


class RegisterApiView(APIView):
    throttle_classes = [RegisterRateThrottle]
    permission_classes = [AllowAny]
    
    def post(self, request):
        serializer = UserCreationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        
        refresh = CustomTokenObtainPairSerializer.get_token(user)

        return Response(
            {'message': 'user created',
             'refresh': str(refresh),
             'access': str(refresh.access_token),
            },

            status=status.HTTP_201_CREATED
        )

class LoginApiView(TokenObtainPairView):
    throttle_classes = [LoginRateThrottle]
    serializer_class = CustomTokenObtainPairSerializer


class logoutApiView(APIView):
    permission_classes = [IsAuthenticated]

    def post(request):
        refresh_token = request.data.get('refresh')
        token = RefreshToken(refresh_token)
        token.blacklist()

        return Response(
            {'message': 'logout is successful'},
            status=status.HTTP_205_RESET_CONTENT
        )






