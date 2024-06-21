from django.urls import path
from .views import SignUp, Longin, CreateFriendRequest, GetFriendRequestsView

urlpatterns = [
    path('signup/', SignUp.as_view(), name='signup'),
    path('login/', Longin.as_view(), name='signup'),
    path('create-friend-req/', CreateFriendRequest.as_view(), name='signup'),
    path('get-friend-req/', GetFriendRequestsView.as_view(), name='signup'),
]
