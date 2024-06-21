from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .manager import UserManager, FriendRequestsManager
from rest_framework.permissions import AllowAny, IsAuthenticated


# Create your views here.
class SignUp(APIView):
    permission_classes = ()

    def post(self, request):
        try:
            UserManager.signup(request)
        except Exception as e:
            return Response({'result': 'Error', 'data': str(e)}, status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response({'result': 'Error', 'data': 'Successfully'})


class Longin(APIView):
    permission_classes = ()

    def post(self, request):
        try:
            UserManager.login_user(request)
        except Exception as e:
            return Response({'result': 'Error', 'data': str(e)}, status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response({'result': 'success', 'data': 'Successfully'})


class CreateFriendRequest(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            FriendRequestsManager.create_friend_req(request)
        except Exception as e:
            return Response({'result': 'Error', 'data': str(e)}, status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response({'result': 'success', 'data': 'friend request created'})


class GetFriendRequestsView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        try:
            data = FriendRequestsManager.get_friend_requests(request)
        except Exception as e:
            return Response({'result': 'Error', 'data': str(e)}, status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response({'result': 'success', 'data':  data})
