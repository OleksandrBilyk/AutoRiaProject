from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import (AllowAny, IsAdminUser, IsAuthenticated,
                                        IsAuthenticatedOrReadOnly)
from rest_framework.response import Response

from apps.cars.models import CarModel, CurrencyModel
from apps.cars.serializers import (CarListSerializer, CarSerializer,
                                   CurrencySerializer)

from .filters import CarFilter


class CarListView(ListAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarListSerializer
    filterset_class = CarFilter
    permission_classes = [AllowAny]


class CarRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, *args, **kwargs):
        car = self.get_object()
        serializer = CarSerializer(car)
        currency_data = CurrencyModel.objects.all()
        cross_course = {arg.ccy: (arg.buy, arg.sale) for arg in currency_data}
        data = serializer.data
        data['cross_course'] = cross_course
        match serializer.data.get('currency'):
            case 'UAH':
                full_price = {'UAH': serializer.data.get('price'),
                              'USD': serializer.data.get('price')/float(cross_course.get('USD')[0]),
                              'EUR': serializer.data.get('price')/float(cross_course.get('EUR')[0])},
                data['full_price'] = full_price
            case 'USD':
                full_price = {'UAH': serializer.data.get('price')*float(cross_course.get('USD')[1]),
                              'USD': serializer.data.get('price'),
                              'EUR': (serializer.data.get('price')*float(cross_course.get('USD')[1])) / float(
                                   cross_course.get('EUR')[0])},
                data['full_price'] = full_price
            case 'EUR':
                full_price = {'UAH': serializer.data.get('price') * float(cross_course.get('EUR')[1]),
                              'USD': (serializer.data.get('price') * float(cross_course.get('EUR')[1])) / float(
                                    cross_course.get('USD')[0]),
                              'EUR': serializer.data.get('price')},
                data['full_price'] = full_price

        return Response(data, status.HTTP_201_CREATED)