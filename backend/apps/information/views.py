
from core.permissions import IsManager, IsSuperUser, IsUser
from core.services.car_statistic import CarStatisticService
from django.contrib.auth import get_user, get_user_model
from django.core.mail import EmailMultiAlternatives
from rest_framework import status
from rest_framework.generics import (GenericAPIView, ListCreateAPIView,
                                     UpdateAPIView, get_object_or_404)
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.response import Response

from apps.cars.models import CarModel, CurrencyModel
from apps.cars.serializers import CarSerializer
from apps.users.serializer import ProfileAvatarSerializer, UserSerializer

from .models import CarViewingModel

UserModel = get_user_model()
class TradingPlatformInformationView(GenericAPIView):
    permission_classes = (AllowAny,)

    def get(self, *args, **kwargs):
        registered_users = UserModel.objects.all().count()
        premium_users = UserModel.objects.filter(is_premium=True).count()
        registered_auto = CarModel.objects.all().count()
        viewing_count = CarViewingModel.objects.all().count()
        context = {'registered_users': registered_users,
                   'premium_users': premium_users,
                   'registered_auto': registered_auto,
                   'viewing_count': viewing_count}
        return Response(context, status.HTTP_200_OK)


class UserCarInformationView(GenericAPIView):
    # queryset = CarModel.objects.all()
    # serializer_class = CarSerializer
    queryset = UserModel.objects.all()
    permission_classes = (IsAuthenticated,)
    def get(self, request, *args, **kwargs):
        user = self.get_object()
        user_serializer = UserSerializer(user)
        if not user_serializer.data.get('is_premium'):
            return Response({'details': 'To view information about the ad, '
                                        'you need to purchase a premium package.'}, status=status.HTTP_200_OK)
        data = self.request.data
        if not data.get('id'):
            return Response(user_serializer.data, status.HTTP_200_OK)
        # car = get_object_or_404(CarModel, id=data.get('id'))
        # car_serializer = CarSerializer(car)

        context = CarStatisticService.car_viewing_count(data)

        return Response(context, status.HTTP_200_OK)

