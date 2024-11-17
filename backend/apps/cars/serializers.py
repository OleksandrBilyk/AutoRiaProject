
from rest_framework import serializers

from apps.cars.models import CarModel, CarPhotoModel, CurrencyModel


class CarPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarPhotoModel
        fields = ('photo',)
        extra_kwargs = {
            'photo': {
                'required': True
            }
        }


class CarSerializer(serializers.ModelSerializer):
    photo_car = CarPhotoSerializer(many=True, read_only=True)
    class Meta:
        model = CarModel
        fields = ('id', 'brand', 'car_model', 'price', 'year', 'created_at', 'updated_at', 'photo_car',
                  'information', 'currency', 'region', 'user')


class CarListSerializer(serializers.ModelSerializer):

    class Meta:
        model = CarModel
        fields = ('id', 'brand', 'year', 'currency')


class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = CurrencyModel
        fields = ('id', 'created_at', 'updated_at', 'ccy', 'buy', 'sale')

