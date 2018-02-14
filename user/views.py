from rest_framework.status import HTTP_200_OK
from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework.response import Response
from rest_framework import generics

from web.settings import ANONYMOUS_USER_ID

# from django.models import User
from django.contrib.auth.models import User
from .serializers import UserSerializer, UserCreationSerializer


class UserList(generics.ListAPIView):
    """
    User list.
    """
    model = User
    serializer_class = UserSerializer

    def get_queryset(self):
        if self.request.user.is_superuser:
            return User.objects.exclude(id=ANONYMOUS_USER_ID)
        return User.objects.filter(id=self.request.user.id)


class UserDetail(generics.RetrieveUpdateAPIView):
    """
    Client detail.
    """
    model = User
    serializer_class = UserSerializer

    def get_queryset(self):
        if self.request.user.is_superuser:
            return User.objects.exclude(id=ANONYMOUS_USER_ID)
        return User.objects.filter(id=self.request.user.id)


class UserCreation(generics.CreateAPIView):
    permission_classes = ()
    model = User
    serializer_class = UserCreationSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            print(serializer.validated_data)
            user = User(email=serializer.validated_data['email'], username=serializer.validated_data['email'])
            user.set_password(serializer.validated_data['password'])
            user.save()
            return Response(UserSerializer(user).data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)



user_list = UserList.as_view()
user_detail = UserDetail.as_view()
user_create = UserCreation.as_view()