from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'brands', BrandListApiView, basename='brand')
router.register(r'categories', CategoryListApiView, basename='category')
router.register(r'products', ProductListApiView, basename='product')
router.register(r'color', ProductColorApiView, basename='color')
router.register(r'images', ProductImageApiView, basename='images')

urlpatterns = [
    path('', include(router.urls)),
    ]