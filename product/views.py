from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .Serializers import *
from rest_framework.permissions import IsAdminUser

class BrandListApiView(ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    permission_classes = [IsAdminUser]


class CategoryListApiView(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer   
    permission_classes = [IsAdminUser]


class ProductListApiView(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = StaffProductSerializer
    permission_classes = [IsAdminUser]

class ProductColorApiView(ModelViewSet):
    queryset = ProductColor.objects.all()
    serializer_class = ProductColorSerializer
    permission_classes = [IsAdminUser]



class ProductImageApiView(ModelViewSet):
    queryset = ProductImages.objects.all()
    serializer_class = ProductImageSerializer
    permission_classes = [IsAdminUser]
