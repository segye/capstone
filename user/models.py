from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.contrib.auth.models import User, PermissionsMixin
from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    email = models.CharField(max_length=40, unique=True, verbose_name="아이디")
    password = models.CharField(max_length=100, verbose_name="비밀번호")
    nickname = models.CharField(max_length=20, unique=True, verbose_name="닉네임")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="회원가입시간")
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()
    USERNAME_FIELD = "email"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = ['nickname']

    def __str__(self):
        return self.email

    class Meta:
        ordering = ['id']
        db_table = 'shopping_user'
        verbose_name = '사용자'
        verbose_name_plural = '사용자'

    @property
    def is_staff(self):
        return self.is_admin
