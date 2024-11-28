import os

from core.permissions import IsManager, IsSuperUser, IsUser
from django.contrib.auth import get_user_model
from django.core.mail import EmailMultiAlternatives
from rest_framework import status
from rest_framework.generics import (GenericAPIView, ListCreateAPIView,
                                     UpdateAPIView)
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from apps.users.models import ProfileModel
from apps.users.serializer import ProfileAvatarSerializer, UserSerializer

UserModel = get_user_model()
class UserListCreateView(ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()
    permission_classes = (AllowAny,)

    # def get_permissions(self):
    #     if self.request.method == 'GET':
    #         return (IsAuthenticated(), )
    #     return (AllowAny(), )


class UserBlockView(GenericAPIView):
    serializer_class = UserSerializer
    permission_classes = (IsManager, IsSuperUser)

    def get_queryset(self):
        return UserModel.objects.exclude(id=self.request.user.id)
    def patch(self, *args, **kwargs):

        user = self.get_object()
        if user.is_active:
            user.is_active = 0
            user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data, status.HTTP_200_OK)


class UserUnBlockView(GenericAPIView):
    serializer_class = UserSerializer
    permission_classes = (IsSuperUser, IsManager)

    def get_queryset(self):
        return UserModel.objects.exclude(id=self.request.user.id)

    def patch(self, *args, **kwargs):
        user = self.get_object()
        if not user.is_active:
            user.is_active = 3
            user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data, status.HTTP_200_OK)


class UserAddAvatarView(UpdateAPIView):
    permission_classes = (IsUser,)
    serializer_class = ProfileAvatarSerializer
    http_method_names = ('put',)

    def get_object(self):
        return self.request.user.profile

    def perform_update(self, serializer):
        profile:ProfileModel = self.get_object()
        profile.avatar.delete()
        super().perform_update(serializer)

