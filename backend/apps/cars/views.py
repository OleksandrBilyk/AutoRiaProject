from rest_framework.generics import (ListAPIView, RetrieveUpdateDestroyAPIView,
                                     UpdateAPIView)
from rest_framework.permissions import (AllowAny, IsAdminUser, IsAuthenticated,
                                        IsAuthenticatedOrReadOnly)

from apps.cars.models import CarModel
from apps.cars.serializers import (CarListSerializer, CarSerializer,
                                   ProfilePhotoCarSerializer)
from apps.users.models import UserModel

from .filters import CarFilter


class CarListView(ListAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarListSerializer
    filterset_class = CarFilter
    permission_classes = [AllowAny]

class UsersAddCarView(GenericAPIView):
    queryset = UserModel.objects.all()
    permission_classes = (IsAuthenticated,)
    def post(self, *args, **kwargs):
        user = self.get_object()
        data = self.request.data
        serializer = CarSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=user)
        user_serializer = UserSerializer(user)
        return Response(serializer.data, status.HTTP_201_CREATED)


class CarRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer


