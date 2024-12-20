from datetime import datetime

from core.services.car_statistic import CarStatisticService
from django.contrib.auth import get_user_model
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from apps.cars.models import CarModel, CurrencyModel
from apps.cars.serializers import CarSerializer, CurrencySerializer
from apps.information.serializer import (CarInformationSerializer,
                                         InformationWebsiteSerializer)
from apps.users.serializer import UserSerializer

from .models import CarViewingModel

UserModel = get_user_model()


class TradingPlatformInformationView(GenericAPIView):
    """
    Get information about the trading platform
    """
    permission_classes = (AllowAny,)

    def get_serializer(self, *args, **kwargs):
        pass

    @swagger_auto_schema(operation_id='Website information',
                         responses={status.HTTP_200_OK: InformationWebsiteSerializer}, security=[])
    def get(self, *args, **kwargs):
        registered_users = UserModel.objects.all().count()
        premium_users = UserModel.objects.filter(is_premium=True).count()
        registered_auto = CarModel.objects.all().count()
        viewing_count = CarViewingModel.objects.all().count()
        currency_serializer_usd = CurrencySerializer(CurrencyModel.objects.filter(ccy='USD').first())
        currency_serializer_eur = CurrencySerializer(CurrencyModel.objects.filter(ccy='EUR').first())
        time_update = currency_serializer_usd.data.get('updated_at')
        timestamp = (datetime.fromisoformat(time_update).isoformat(" ", "seconds")
                     .replace("+00:00", ""))
        data = {'registered_users': registered_users,
                'premium_users': premium_users,
                'registered_auto': registered_auto,
                'viewing_count': viewing_count,
                'exchange_rate_update_time': timestamp,
                'USD_exchange_rate_buy': currency_serializer_usd.data.get('buy'),
                'USD_exchange_rate_sale': currency_serializer_usd.data.get('sale'),
                'EUR_exchange_rate_buy': currency_serializer_eur.data.get('buy'),
                'EUR_exchange_rate_sale': currency_serializer_eur.data.get('sale')
                }
        return Response(data, status.HTTP_200_OK)


class UserCarInformationView(GenericAPIView):
    """
        Get information about the car: number of views and average price for a given car model
    """
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer
    permission_classes = (IsAuthenticated,)

    @swagger_auto_schema(operation_id='Car information', responses={status.HTTP_200_OK: CarInformationSerializer},
                         manual_parameters=[openapi.Parameter(name='day', in_=openapi.IN_QUERY,
                                                              description='the number of days for which you want'
                                                                          ' to get the number of views',
                                                              required=False, type='str', default='today'),
                                            openapi.Parameter(name='week', in_=openapi.IN_QUERY,
                                                              description='the number of week for which you want'
                                                                          ' to get the number of views',
                                                              required=False, type='str', default='this week'),
                                            openapi.Parameter(name='month', in_=openapi.IN_QUERY,
                                                              description='the number of month for which you want'
                                                                          ' to get the number of views',
                                                              required=False, type='str', default='this month')
                                            ])
    def get(self, request, *args, **kwargs):
        user = self.request.user
        user_serializer = UserSerializer(user)
        if not user_serializer.data.get('is_premium'):
            return Response({'details': 'To view information about the ad, '
                                        'you need to purchase a premium package.'}, status=status.HTTP_200_OK)
        car = self.get_object()
        car_serializer = CarSerializer(car)
        request_data = self.request.data
        viewing_statistic = CarStatisticService.car_viewing_count(car_id=car_serializer.data.get('id'),
                                                                  request_data=request_data)
        price_statistic = CarStatisticService.car_price_statistic(car)
        data = {
            'car': car_serializer.data,
            'viewing_statistic': viewing_statistic,
            'price_statistic': price_statistic
        }
        return Response(data, status.HTTP_200_OK)

