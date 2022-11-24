from rest_framework import serializers

from product.models import Product
from .models import Shoppingcart


class CartSerializer(serializers.ModelSerializer):

    class Meta:
        model = Shoppingcart
        fields = '__all__'
