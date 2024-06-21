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

        return Response({'result': 'success', 'data': 'Successfully'}, status.HTTP_200_OK)


class Longin(APIView):
    permission_classes = ()

    def post(self, request):
        try:
            UserManager.login_user(request)
        except Exception as e:
            return Response({'result': 'Error', 'data': str(e)}, status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response({'result': 'success', 'data': 'Successfully'}, status.HTTP_200_OK)


class CreateFriendRequest(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            FriendRequestsManager.validate(request)
            FriendRequestsManager.create_friend_req(request)
        except Exception as e:
            return Response({'result': 'Error', 'data': str(e)}, status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response({'result': 'success', 'data': 'friend request created'}, status.HTTP_200_OK)


class ApproveFriendRequest(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            user = FriendRequestsManager.accept_friend_req(request)
        except Exception as e:
            return Response({'result': 'Error', 'data': str(e)}, status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response({'result': 'success', 'data': 'friend request accepted'}, status.HTTP_200_OK)


class GetFriendRequestsInvitesView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        try:
            data = FriendRequestsManager.get_friend_requests(request, 'to')
        except Exception as e:
            return Response({'result': 'Error', 'data': str(e)}, status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response({'result': 'success', 'data': data}, status.HTTP_200_OK)


class GetFriendRequestsFromYouView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        try:
            data = FriendRequestsManager.get_friend_requests(request, 'from')
        except Exception as e:
            return Response({'result': 'Error', 'data': str(e)}, status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response({'result': 'success', 'data': data}, status.HTTP_200_OK)


class GetUsersFilter(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        try:
            data, number_of_pages, number_of_records = UserManager.get_user_by_name_and_email(request)
        except Exception as e:
            return Response({'result': 'Error', 'data': str(e)}, status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response({'result': 'success', 'data': data, 'number_of_pages': number_of_pages,
                         "number_of_records": number_of_records}, status.HTTP_200_OK)


class DeleteRejectFriendReq(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            user = FriendRequestsManager.delete_reject_friend_req(request)
        except Exception as e:
            return Response({'result': 'Error', 'data': str(e)}, status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response({'result': 'success',
                         'data': 'Friend of User {} is {} Successfully '.fromat(user, request.data.get('type'))},
                        status.HTTP_200_OK)


class GetFriends(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        try:
            data = FriendRequestsManager.get_friends(request)
        except Exception as e:
            return Response({'result': 'Error', 'data': str(e)}, status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response({'result': 'success', 'data': data}, status.HTTP_200_OK)
