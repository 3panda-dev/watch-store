from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

# router = DefaultRouter()

# router.register(r'user', CreateUserApiView, basename='user')

urlpatterns = [
    path('register/', CreateUserApiView.as_view(), name='register')
    
]


