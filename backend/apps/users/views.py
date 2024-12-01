from core.pagination import PagePagination
from core.permissions import IsManager, IsSuperUser, IsUser
from django.contrib.auth import get_user_model
from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.generics import (GenericAPIView, ListCreateAPIView,
                                     UpdateAPIView)
from rest_framework.response import Response

from apps.users.models import ProfileModel
from apps.users.serializer import ProfileAvatarSerializer, UserSerializer

UserModel = get_user_model()


@method_decorator(name='post', decorator=swagger_auto_schema(security=[]))
class UserListCreateView(ListCreateAPIView):
    """
        get:
            Create a list of all users
        post:
            Create a new user
    """
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()
    pagination_class = PagePagination
    permission_classes = (IsManager, IsSuperUser)


class UserBlockView(GenericAPIView):
    """
    Admin can block users
    """
    serializer_class = UserSerializer
    permission_classes = (IsManager, IsSuperUser)

    def get_serializer(self, *args, **kwargs):
        pass

    def get_queryset(self):
        return UserModel.objects.exclude(id=self.request.user.id)

    @swagger_auto_schema(operation_id='Block user', responses={status.HTTP_200_OK: UserSerializer})
    def patch(self, *args, **kwargs):

        user = self.get_object()
        if user.is_active:
            user.is_active = 0
            user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data, status.HTTP_200_OK)


class UserUnBlockView(GenericAPIView):
    """
        Admin can unblock users
    """
    serializer_class = UserSerializer
    permission_classes = (IsSuperUser, IsManager)

    def get_queryset(self):
        return UserModel.objects.exclude(id=self.request.user.id)

    def get_serializer(self, *args, **kwargs):
        pass

    @swagger_auto_schema(operation_id='UnBlock user', responses={status.HTTP_200_OK: UserSerializer})
    def patch(self, *args, **kwargs):
        user = self.get_object()
        if not user.is_active:
            user.is_active = 3
            user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data, status.HTTP_200_OK)


class UserAddAvatarView(UpdateAPIView):
    """
    User can add avatar
    """
    permission_classes = (IsUser,)
    serializer_class = ProfileAvatarSerializer
    http_method_names = ('put',)

    def get_object(self):
        return self.request.user.profile

    def perform_update(self, serializer):
        profile:ProfileModel = self.get_object()
        profile.avatar.delete()
        super().perform_update(serializer)

    @swagger_auto_schema(operation_id='Add avatar to user', responses={status.HTTP_200_OK: UserSerializer})
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

