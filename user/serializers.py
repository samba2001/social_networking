from rest_framework.serializers import ModelSerializer
from .models import User, FriendsRequests


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'email', 'mobile']


class FriendRequestsToUserSerializer(ModelSerializer):
    to_user = UserSerializer()

    class Meta:
        model = FriendsRequests
        fields = "__all__"

class FriendRequestsFromUserSerializer(ModelSerializer):
    from_user = UserSerializer()

    class Meta:
        model = FriendsRequests
        fields = "__all__"

