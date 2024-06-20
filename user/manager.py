from .models import User
from django.contrib.auth import authenticate, login, logout


class UserManager:
    @staticmethod
    def login_user(request):
        data = request.data
        user = User.objects.get(email=data.get('email'))
        if not user:
            raise Exception('User does not exists')
        user = authenticate(request, email=data.get('email'), password=data.get('password'))
        if user:
            login(request, user)
            return
        raise Exception('invalid credentials')

    @staticmethod
    def signup(request):
        data = request.data
        user = User(
            email=data.get('email'),
            name=data.get('name'),
            mobile=data.get('mobile'),
            password=data.get('password'),
        )
        temp = User.objects.all()
        user.save()
