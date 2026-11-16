from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'brands', BrandListCreateView, basename='brand')
router.register(r'categories', CategoryListCreateView, basename='category')
router.register(r'products', ProductListCreateView, basename='product')

urlpatterns = [
    path('', include(router.urls)),
    ]