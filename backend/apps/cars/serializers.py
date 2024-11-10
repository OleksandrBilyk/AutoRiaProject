
from rest_framework import serializers

from apps.cars.models import CarModel, CurrencyModel


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = ('id', 'brand', 'car_model', 'price', 'year', 'created_at', 'updated_at', 'photo_car',
                  'information', 'currency', 'region', 'user')


class ProfilePhotoCarSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = ('photo_car',)
        extra_kwargs = {'photo_car': {'required': True}}


class CarListSerializer(serializers.ModelSerializer):

    class Meta:
        model = CarModel
        fields = ('id', 'brand', 'year', 'currency')


class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = CurrencyModel
        fields = ('id', 'created_at', 'updated_at', 'ccy', 'buy', 'sale')

