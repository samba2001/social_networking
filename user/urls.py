from django.urls import path
from .views import SignUp, Longin

urlpatterns = [
    path('signup/', SignUp.as_view(), name='signup'),
    path('login/', Longin.as_view(), name='signup'),
]
