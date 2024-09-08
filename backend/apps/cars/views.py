from rest_framework.generics import (ListAPIView, RetrieveUpdateDestroyAPIView,
                                     UpdateAPIView)
from rest_framework.permissions import (AllowAny, IsAdminUser, IsAuthenticated,
                                        IsAuthenticatedOrReadOnly)

from apps.cars.models import CarModel
from apps.cars.serializers import (CarListSerializer, CarSerializer,
                                   ProfilePhotoCarSerializer)

from .filters import CarFilter


class CarListView(ListAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarListSerializer
    filterset_class = CarFilter


class CarRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer


