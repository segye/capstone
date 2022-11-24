import json
from json import JSONDecodeError
import socket

from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import MultipleObjectsReturned
from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics, mixins, viewsets
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from product.models import Product
from user.models import User
from user.utils import login_required2
from .models import Shoppingcart
from django.http import HttpResponse

from .serializer import CartSerializer


class CartView(APIView):
    permissions_classes = [IsAuthenticated]

    def get(self, request):
        user = self.request.user
        carts = Shoppingcart.objects.filter(user=user)

        if not carts.exists():
            return Response({"message": "CART_NOT_EXIST"}, status=404)

        result = [{
            'cart_id': cart.id,
            'product_name': cart.product.name,
            'product_image_url': "http://127.0.0.1:8000" + cart.product.image.url,
            'price': cart.product.price,
            'quantity': cart.quantity,
            'item_total': cart.product.price * cart.quantity,
        } for cart in carts]

        total_bill = int(sum(cart['item_total'] for cart in result))

        return Response({
            "data": result,
            "total_bill": total_bill}, status=200)

    def post(self, request):
        try:
            user = self.request.user
            quantity = request.data["quantity"]
            product_id = request.data["product.id"]

            if Shoppingcart.objects.filter(user=user, product_id=product_id).exists():
                cart = Shoppingcart.objects.filter(user=user).get(product_id=product_id)
                cart.quantity += quantity
                cart.save()
                return Response({"message": "PRODUCT_QUANTITY_UPDATED"}, status=201)

            Shoppingcart.objects.create(
                user=user,
                product_id=product_id,
                quantity=quantity
            )
            return Response({"message": "CART_CREATED"}, status=201)

        except KeyError:
            return Response({"message": "KEY_ERROR"}, status=400)

        except json.JSONDecodeError:
            return Response({"message": "JSON_DECODE_ERROR"}, status=400)

    def patch(self, request):
        try:
            user = self.request.user
            product_id = request.data['product.id']
            quantity = request.data['quantity']

            if not Shoppingcart.objects.filter(user=user, product_id=product_id).exists():
                return Response({"message": "CART_NOT_EXIST"}, status=404)

            cart = Shoppingcart.objects.get(user=user, product_id=product_id)
            cart.quantity = quantity
            cart.save()

            if cart.quantity <= 0:
                return Response({"message": "PRODUCT_QUANTITY_ERROR"}, status=400)

            return Response({"message": "SUCCESS"}, status=201)

        except Shoppingcart.DoesNotExist:
            return Response({"message": "CART_NOT_EXIST"}, status=404)

        except KeyError:
            return Response({"message": "KEY_ERROR"}, status=400)

        except json.JSONDecodeError:
            return Response({"message": "JSON_DECODE_ERROR"}, status=400)

    def delete(self, request):
        try:
            user = self.request.user
            cart_id = request.data.get('id')

            if not Shoppingcart.objects.filter(user=user, id=cart_id).exists():
                return Response({"message": "INVALID_CART", "id:": cart_id}, status=404)

            cart = Shoppingcart.objects.get(id=cart_id, user=user)

            cart.delete()
            return Response({"message": "SUCCESS", "id:": Shoppingcart.id}, status=200)

        except MultipleObjectsReturned:
            return Response({'message': 'MULTIPLE_OBJECTS_RETURNED', }, status=400)
        except ValueError:
            return Response({'message': 'VALUE_ERROR'}, status=400)


class CartDetailAPIView(RetrieveAPIView):
    queryset = Shoppingcart.objects.all()
    serializer_class = CartSerializer

    def get(self, request, *args, **kwargs):
        print(kwargs)
        return self.retrieve(request, *args, **kwargs)

    def delete(self, request, pk):
        try:
            user = self.request.user
            cart_id = pk

            if not Shoppingcart.objects.filter(user=user, id=cart_id).exists():
                return Response({"message": "INVALID_CART", "id:": cart_id}, status=404)

            cart = Shoppingcart.objects.get(id=cart_id, user=user)

            cart.delete()
            return Response({"message": "SUCCESS", "id:": Shoppingcart.id}, status=200)

        except MultipleObjectsReturned:
            return Response({'message': 'MULTIPLE_OBJECTS_RETURNED', }, status=400)
        except ValueError:
            return Response({'message': 'VALUE_ERROR'}, status=400)