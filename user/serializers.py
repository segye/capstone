from django.contrib.auth.hashers import make_password

from .models import User
from rest_framework import serializers


class SignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = User.objects.create(email=validated_data['email'], nickname=validated_data['nickname'],
            password=validated_data['password'])
        #user.password = make_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        model = User
        fields = ["pk", "email", "password", "nickname"]

#class LoginSerializer(serializers.ModelSerializer):
