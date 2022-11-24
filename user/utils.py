from django.http import HttpResponseForbidden
from django.shortcuts import redirect

from user.models import User


def login_required2(func):
    def wrap(request, *args, **kwargs):
        user = request.get('User')
        if user is None or not user:
            return redirect('http://127.0.0.1:8000/admin/login/')
        return func(request, *args, **kwargs)
    return wrap
