
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from core.custom_throttle import LoginRateThrottle, RegisterRateThrottle
from rest_framework_simplejwt.exceptions import TokenError

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


class LogoutApiView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):

        try:
            refresh_token = request.data.get('refresh')

            if refresh_token is None or refresh_token.strip() == '':
                return Response(
                    {'message': 'Refresh token is required'},
                    status=status.HTTP_400_BAD_REQUEST
                )

            token = RefreshToken(refresh_token)

            if token.payload.get('user_id') != request.user.id:
                return Response(
                    {'message': 'Invalid refresh token for the current user'},
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            token.blacklist()

        except TokenError as e:
            return Response(
                {'message': 'Invalid refresh token'},
                status=status.HTTP_400_BAD_REQUEST
            )

        return Response(
            {'message': 'logout is successful'},
            status=status.HTTP_205_RESET_CONTENT
        )






