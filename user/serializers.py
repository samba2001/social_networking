from rest_framework.serializers import ModelSerializer
from .models import User, FriendsRequests


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'email', 'mobile']


class FriendRequestsSerializer(ModelSerializer):
    to_user = UserSerializer()

    class Meta:
        model = FriendsRequests
        fields = ['to_user']
