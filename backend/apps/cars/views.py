from core.services.currency_service import CurrencyService
from core.services.email_service import EmailService
from core.services.profanity_service import NoProfanityService
from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.generics import (GenericAPIView, ListAPIView,
                                     RetrieveUpdateDestroyAPIView)
from rest_framework.permissions import (AllowAny, IsAuthenticated,
                                        IsAuthenticatedOrReadOnly)
from rest_framework.response import Response

from apps.cars.models import CarModel
from apps.cars.serializers import (CarListSerializer, CarPhotoSerializer,
                                   CarSerializer)
from apps.users.models import UserModel
from apps.users.serializer import UserSerializer

from .filters import CarFilter


@method_decorator(name='get', decorator=swagger_auto_schema(security=[]))
class CarListView(ListAPIView):
    """
    List all cars in base
    """
    queryset = CarModel.objects.all()
    serializer_class = CarListSerializer
    filterset_class = CarFilter
    permission_classes = [AllowAny]


class CreateCarView(GenericAPIView):
    queryset = UserModel.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = CarSerializer

    def post(self, *args, **kwargs):
        user = self.request.user
        user_serializer = UserSerializer(user)
        data = self.request.data
        data = data.copy()
        data['user'] = user_serializer.data.get('id')
        serializer = CarSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        no_profanity_data = NoProfanityService.no_profanity_check(user=user, data=data)
        if isinstance(no_profanity_data, bool):
            if not user_serializer.data.get('is_premium'):
                CarModel.objects.filter(user_id=user_serializer.data.get('id')).delete()
                EmailService.payment(user)
            if serializer.validated_data.get('brand') == 'Other':
                serializer.save(user=user)
                return Response('The car ad has been added with the manufacturer brand "Other". '
                                'To add your car brand, please contact the support chat', status.HTTP_201_CREATED)
            serializer.save(user=user)
            return Response(serializer.data, status.HTTP_201_CREATED)
        else:
            return Response({'details': no_profanity_data}, status=status.HTTP_400_BAD_REQUEST)


class CarRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, *args, **kwargs):
        car = self.get_object()
        serializer = CarSerializer(car)
        data = serializer.data
        CurrencyService.add_currency_to_car(data)
        car.car_view.create()
        return Response(data, status.HTTP_201_CREATED)

    def put(self, request, *args, **kwargs):
        car = self.get_object()
        user = self.request.user
        user_serializer = UserSerializer(user)
        data = self.request.data
        data = data.copy()
        data['user'] = user_serializer.data.get('id')
        serializer = CarSerializer(car, data=data)
        serializer.is_valid(raise_exception=True)
        no_profanity_data = NoProfanityService.no_profanity_check(user=user, data=data)
        if isinstance(no_profanity_data, bool):
            serializer.save(user=user)
            return Response(serializer.data, status.HTTP_201_CREATED)
        else:
            return Response({'details': no_profanity_data}, status=status.HTTP_400_BAD_REQUEST)


class CarAddPhotosView(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = CarModel.objects.all()

    def put(self, *args, **kwargs):
        files = self.request.FILES
        car = self.get_object()
        for index in files:
            serializer = CarPhotoSerializer(data={'photo': files[index]})
            serializer.is_valid(raise_exception=True)
            serializer.save(car=car)
        car_serializer = CarSerializer(car)
        return Response(car_serializer.data, status=status.HTTP_200_OK)