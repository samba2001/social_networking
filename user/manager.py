from .models import User, FriendsRequests
from django.contrib.auth import authenticate, login, logout
from .serializers import FriendRequestsSerializer

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


class FriendRequestsManager:
    @staticmethod
    def create_friend_req(request):
        data = request.data
        to_user = User.objects.get(email=data.get('email'))
        if not to_user:
            raise Exception('requested user does not exist')
        if request.user.email == data.get('email'):
            raise Exception('from user and to user cannot be same')
        friendrequest = FriendsRequests(from_user=request.user, to_user=to_user)
        friendrequest.save()
        print(friendrequest)

    @staticmethod
    def get_friend_requests(request):
        data = FriendsRequests.all_objects.filter(from_user__email=request.user.email)
        return FriendRequestsSerializer(data, many=True).data
