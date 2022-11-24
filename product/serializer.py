from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["pk", "name", "price", "stock", "image", "category"]


class ProductdetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["pk", "name", "price", "stock", "description", "image", "category"]
