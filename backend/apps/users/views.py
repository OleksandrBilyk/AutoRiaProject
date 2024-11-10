import os

from core.permissions import IsManager, IsSuperUser, IsUser
from core.services.email_service import EmailService
from core.services.profanity_service import NoProfanityService
from django.contrib.auth import get_user_model
from django.core.mail import EmailMultiAlternatives
from rest_framework import status
from rest_framework.generics import (GenericAPIView, ListCreateAPIView,
                                     UpdateAPIView)
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.response import Response

from apps.cars.models import CarModel
from apps.cars.serializers import CarSerializer
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
    permission_classes = (IsSuperUser, IsManager)

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


class UsersAddCarView(GenericAPIView):
    queryset = UserModel.objects.all()
    permission_classes = (IsAuthenticated,)
    def post(self, *args, **kwargs):
        user = self.get_object()
        user_serializer = UserSerializer(user)
        data = self.request.data
        no_profanity_data = NoProfanityService.no_profanity_check(user=user, data=data)
        if no_profanity_data == 0:
            return Response({'details': 'User is not active, please send message to admin for unban'},
                            status=status.HTTP_400_BAD_REQUEST)
        elif no_profanity_data == 2 or no_profanity_data == 1:
            print(no_profanity_data)
            return Response({'details': f'In your ad, the system found obscene language, '
                                f'you have {no_profanity_data} attempts to change the ad'}, status.HTTP_400_BAD_REQUEST)
        else:
            serializer = CarSerializer(data=no_profanity_data)
            serializer.is_valid(raise_exception=True)
            if not user_serializer.data.get('is_premium'):
                CarModel.objects.filter(user_id=user_serializer.data.get('id')).delete()
                EmailService.payment(user)
            serializer.save(user=user)
            return Response(serializer.data, status.HTTP_201_CREATED)



