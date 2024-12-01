from rest_framework import serializers

from apps.cars.serializers import CarSerializer
from apps.information.models import CarViewingModel


class CarViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarViewingModel
        fields = ('id', 'created_at', 'car')


class ViewingStatisticSerializer(serializers.Serializer):
    car_viewing_all_time = serializers.IntegerField()
    car_viewing_by_month = serializers.IntegerField()
    car_viewing_by_week = serializers.IntegerField()
    car_viewing_by_day = serializers.IntegerField()


class AverageStatisticSerializer(serializers.Serializer):
    UAH = serializers.IntegerField()
    USD = serializers.IntegerField()
    EUR = serializers.IntegerField()


class PriceStatisticSerializer(serializers.Serializer):
    average_cost_model_Ukraine = AverageStatisticSerializer()
    average_cost_model_region = AverageStatisticSerializer()


class InformationWebsiteSerializer(serializers.Serializer):
    registered_users = serializers.IntegerField()
    premium_users = serializers.IntegerField()
    registered_auto = serializers.IntegerField()
    viewing_count = serializers.IntegerField()
    exchange_rate_update_time = serializers.CharField()
    USD_exchange_rate_buy = serializers.IntegerField()
    USD_exchange_rate_sale = serializers.IntegerField()
    EUR_exchange_rate_buy = serializers.IntegerField()
    EUR_exchange_rate_sale = serializers.IntegerField()


class CarInformationSerializer(serializers.Serializer):
    car_serializer = CarSerializer()
    viewing_statistic = ViewingStatisticSerializer()
    price_statistic = PriceStatisticSerializer()
