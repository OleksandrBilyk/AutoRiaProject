from rest_framework import serializers

from apps.information.models import CarViewingModel


class CarViewSerializer(serializers.ModelSerializer):

    class Meta:
        model = CarViewingModel
        fields = ('id', 'created_at', 'car')
