from django.urls import path

from apps.cars.views import (CarAddPhotosView, CarListView,
                             CarRetrieveUpdateDestroyView)

urlpatterns = [
    path('', CarListView.as_view(), name='cars_list'),
    path('/<int:pk>', CarRetrieveUpdateDestroyView.as_view(), name='cars_retrieve_update_delete'),
    path('/<int:pk>/photos', CarAddPhotosView.as_view(), name='cars_add_photos'),
]