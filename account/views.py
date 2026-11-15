
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from django.contrib.auth import login, logout

from .serializers import *


class CreateUserApiView(APIView):
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



