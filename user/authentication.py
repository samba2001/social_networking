from django.contrib.auth.backends import ModelBackend
from .models import User


class UserAuthentication(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        user = User.objects.get(email=request.data.get('email').lower())
        if user.password == request.data.get('password'):
            return user
        else:
            raise Exception('Invalid credentials')
