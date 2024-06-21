from django.urls import path

from .views import SignUp, Longin, CreateFriendRequest, GetFriendRequestsInvitesView, \
    GetFriendRequestsFromYouView, GetUsersFilter, DeleteRejectFriendReq, GetFriends, ApproveFriendRequest

urlpatterns = [
    path('signup/', SignUp.as_view(), name='signup'),
    path('login/', Longin.as_view(), name='login'),
    path('create-friend-req/', CreateFriendRequest.as_view(), name='create-friend-req'),
    path('approve-friend-req/', ApproveFriendRequest.as_view(), name='approve-friend-req'),
    path('get-friend-req-invites/', GetFriendRequestsInvitesView.as_view(), name='get-friend-req'),
    path('get-your-friend-req/', GetFriendRequestsFromYouView.as_view(), name='get-friend-req'),
    path('get-users-filter/', GetUsersFilter.as_view(), name='get-users-filter'),
    path('delete-reject-friend-req/', DeleteRejectFriendReq.as_view(), name='delete-reject-friend-req'),
    path('get-friends/', GetFriends.as_view(), name='get-friends'),
]
