from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .Serializers import *
from rest_framework.permissions import IsAdminUser

class BrandListCreateView(ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    permission_classes = [IsAdminUser]


class CategoryListCreateView(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer   
    permission_classes = [IsAdminUser]


class ProductListCreateView(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = StaffProductSerializer
    permission_classes = [IsAdminUser]