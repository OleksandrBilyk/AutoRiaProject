from django.urls import path

from apps.cars.views import (CarAddPhotosView, CarListView,
                             CarRetrieveUpdateDestroyView, CreateCarView)

urlpatterns = [
    path('', CarListView.as_view(), name='cars_list'),
    path('/create', CreateCarView.as_view(), name='car_create'),
    path('/<int:pk>', CarRetrieveUpdateDestroyView.as_view(), name='cars_retrieve_update_delete'),
    path('/<int:pk>/photos', CarAddPhotosView.as_view(), name='cars_add_photos'),
]