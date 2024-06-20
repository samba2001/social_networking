from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .manager import UserManager


# Create your views here.
class SignUp(APIView):
    permission_classes = ()

    @staticmethod
    def post(request):
        try:
            UserManager.signup(request)
        except Exception as e:
            return Response({'result': 'Error', 'data': str(e)}, status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response({'result': 'Error', 'data': 'Successfully'})


class Longin(APIView):
    permission_classes = ()

    @staticmethod
    def post(request):
        try:
            UserManager.login_user(request)
        except Exception as e:
            return Response({'result': 'Error', 'data': str(e)}, status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response({'result': 'Error', 'data': 'Successfully'})
