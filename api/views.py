# -*- coding: utf-8 -*-
from rest_framework.status import HTTP_200_OK
from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework import generics
from rest_framework.response import Response
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.contrib.auth import login
from django.utils import timezone
from django.conf import settings

from django.contrib.auth.models import Group
# from client.serializers import ClientSerializer
from user.serializers import UserSerializer
from .models import Token
from .serializers import AuthTokenSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

class ApiLogin(generics.GenericAPIView):
    """
    In response you get "Set-Cookie" with session id, which can use in
    Session Authentication. And you get User serializer object.
    """
    # authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = ()
    model = settings.AUTH_USER_MODEL
    serializer_class = AuthTokenSerializer

    # @csrf_exempt
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            login(request, user)
            print('test')
            return Response(UserSerializer(user).data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class ObtainAuthToken(generics.GenericAPIView):
    """
    In response you get:
    token -- key 48 character
    expires -- in seconds
    expires_date -- after this date the token is invalid
    user -- User serializer object
    """
    permission_classes = ()
    serializer_class = AuthTokenSerializer
    model = Token

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        #group = Group.objects.get(name='adminusers')
        if serializer.is_valid():
            user = serializer.validated_data['user']
            Token.objects.filter(user=user, expires__lt=timezone.now()).delete()
            token, created = Token.objects.get_or_create(user=user)

            return Response({'token': token.key, 'expires': 2400,
                'expires_date': token.expires.strftime('%Y-%m-%d %H:%M:%S'),
                'user': UserSerializer(user).data})
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

apilogin = ApiLogin.as_view()
obtain_auth_token = ObtainAuthToken.as_view()
