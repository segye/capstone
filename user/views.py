from tokenize import Token

from django.contrib.auth import authenticate
from django.shortcuts import render
from django.views.generic import CreateView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND, HTTP_200_OK

from .models import User
from .serializers import SignupSerializer


class SignupView(CreateAPIView):
    model = User
    serializer_class = SignupSerializer
    permission_classes = [
        AllowAny,
    ]


@api_view(['POST'])
@permission_classes((AllowAny,))
def login(request):
    email = request.data.get('email')
    password = request.data.get('password')

    if email is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)

    # 여기서 authenticate로 유저 validate
    user = authenticate(email=email, password=password)

    if not user:
        return Response({'error': 'Invalid credentials'}, status=HTTP_404_NOT_FOUND)

    # user 로 토큰 발행
    token, _ = Token.objects.get_or_create(user=user)

    return Response({'token': token.key}, status=HTTP_200_OK)
