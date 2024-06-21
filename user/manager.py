from .models import User, FriendsRequests
from django.contrib.auth import authenticate, login, logout
from .serializers import FriendRequestsFromUserSerializer, FriendRequestsToUserSerializer, UserSerializer
from django.db.models import Q, Prefetch
from datetime import datetime, timezone
from utils.pagination import custom_paginator


class UserManager:
    @staticmethod
    def login_user(request):
        data = request.data
        user = User.objects.filter(email__iexact=data.get('email').lower())
        if not user:
            raise Exception('User does not exists')
        user = authenticate(request, email=data.get('email').lower(), password=data.get('password'))
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

    @staticmethod
    def get_user_by_name_and_email(request):
        query = Q()
        data = request.query_params
        # text = data.get('name') if data.get('name') else data.get('email')
        if data.get('email'):
            query |= Q(email__iexact=data.get('email'))
        if data.get('name'):
            query |= Q(name__icontains=data.get('name'))
        data = User.objects.filter(query)
        data, number_of_pages, count_of_records = custom_paginator(request.query_params, data)
        data = UserSerializer(data, many=True).data
        return data, number_of_pages, count_of_records


class FriendRequestsManager:
    @staticmethod
    def create_friend_req(request):
        data = request.data
        to_user = User.objects.get(email__iexact=data.get('email'))
        if not to_user:
            raise Exception('requested user does not exist')
        if request.user.email == data.get('email'):
            raise Exception('from user and to user cannot be same')
        friendrequest = FriendsRequests(from_user=request.user, to_user=to_user)
        friendrequest.save()
        print(friendrequest)

    @staticmethod
    def validate(request):
        last_two_friend_requests = FriendsRequests.all_objects.filter(from_user_id=request.user.id).order_by(
            '-created_at')[:2]
        if len(last_two_friend_requests) == 2:
            if abs((last_two_friend_requests[1].created_at.replace(tzinfo=timezone.utc)
                    - datetime.now(timezone.utc))).total_seconds() / 60 <= 1:
                raise Exception('Your can not create more than 2 friend request in a single minute try after some time')
        existing_req = FriendsRequests.all_objects.filter(
            Q(from_user__email=request.data.get('email')) | Q(to_user__email=request.data.get('email').lower()))
        if len(existing_req):
            raise Exception('There is an existing request with user')

    @staticmethod
    def accept_friend_req(request):
        data = request.data
        req_obj = FriendsRequests.all_objects.filter(id=data.get('id'))
        if not req_obj:
            raise Exception('there is no friend request')
        req_obj = req_obj[0]
        if request.user.id == req_obj.from_user_id:
            raise Exception('request created by you cannot br accepted by you ')
        if not req_obj.status == 'CRE':
            raise Exception('this friend request is already {}'.format(req_obj.status))
        req_obj.status = 'APP'
        req_obj.save()
        return req_obj.to_user

    @staticmethod
    def get_friend_requests(request, mode='from'):
        if mode == 'from':
            from_you = FriendsRequests.all_objects.filter(from_user__email=request.user.email.lower(), status='CRE')
            return FriendRequestsToUserSerializer(from_you, many=True).data,
        to_you = FriendsRequests.all_objects.filter(to_user__email=request.user.email.lower(), status='CRE')
        return FriendRequestsFromUserSerializer(to_you,
                                                many=True).data

    @staticmethod
    def delete_reject_friend_req(request):
        data = request.data
        friend_req = FriendsRequests.all_objects.get(id=data.get('id'))
        if data.get('type') == 'REJECT':
            friend_req.status('REJ')
            friend_req.save()
            return
        friend_req.delete()

    @staticmethod
    def get_friends(request):
        from_user_id = FriendsRequests.all_objects.filter(
            Q(from_user__id=request.user.id) & Q(status='APP')).values_list('from_user_id', flat=True)
        to_user_id = FriendsRequests.all_objects.filter(Q(to_user__id=request.user.id) & Q(status='APP')).values_list(
            'to_user_id', flat=True)
        from_user_id = list(from_user_id)
        from_user_id.extend(list(to_user_id))
        users = User.all_objects.filter(id__in=from_user_id)
        return UserSerializer(users, many=True).data
