
from rest_framework import serializers

from apps.cars.models import CarModel


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = ('id', 'brand', 'price', 'year', 'body_type', 'created_at', 'updated_at', 'photo_car')


class ProfilePhotoCarSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = ('photo_car',)
        extra_kwargs = {'photo_car': {'required': True}}


class CarListSerializer(serializers.ModelSerializer):

    class Meta:
        model = CarModel
        fields = ('id', 'brand', 'year', 'user')
        depth = 1

