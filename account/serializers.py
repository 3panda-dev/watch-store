from .models import *
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class UserCreationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['phone', 'email', 'password']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['email'] = user.email
        token['phone'] = user.phone

        return token
