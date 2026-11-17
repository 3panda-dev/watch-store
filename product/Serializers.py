from .models import *
from rest_framework.serializers import ModelSerializer

class ProductColorSerializer(ModelSerializer):
    class Meta:
        model = ProductColor
        fields = "__all__"


class ProductImageSerializer(ModelSerializer):
    class Meta:
        model = ProductImages
        fields = "__all__"


class BrandSerializer(ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at']


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at']



class StaffProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        read_only_fields = ['id', 'slug', 'created_at', 'updated_at']

# class ProductSerializer(ModelSerializer):
#     class Meta:
#         model = product
#         fields = []