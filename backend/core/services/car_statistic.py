
from datetime import date, datetime

from apps.cars.models import CarModel
from apps.cars.serializers import CarSerializer
from apps.information.models import CarViewingModel
from core.services.currency_service import CurrencyService
from rest_framework.generics import get_object_or_404


class CarStatisticService:
    @staticmethod
    def car_viewing_count(car_id, request_data):
        car_viewing = CarViewingModel.objects.filter(car_id=car_id)
        car_viewing_all_time = car_viewing.count()
        car_viewing_by_day = car_viewing.filter(created_at__day=request_data.get('day')) if request_data.get('day') \
            else car_viewing.filter(created_at__day=date.today().day)
        car_viewing_by_month = car_viewing.filter(created_at__month=request_data.get('month')) if request_data.get('month') \
            else car_viewing.filter(created_at__month=date.today().month)
        car_viewing_by_week = car_viewing.filter(created_at__week=request_data.get('week')) if request_data.get('week') \
            else car_viewing.filter(created_at__week=datetime.now().isocalendar().week)
        context = {'car_viewing_all_time': car_viewing_all_time,
                   'car_viewing_by_month': car_viewing_by_month.count(),
                   'car_viewing_by_week,': car_viewing_by_week.count(),
                   'car_viewing_by_day': car_viewing_by_day.count()}
        return context
    @staticmethod
    def car_price_statistic(car):
        car_serializer = CarSerializer(car)
        cars_this_model_all = (CarModel.objects.exclude(id=car_serializer.data.get('id')).
                               filter(car_model=car_serializer.data.get('car_model')))
        cars_this_model_all_serializer = CarSerializer(cars_this_model_all, many=True)
        if not cars_this_model_all_serializer.data:
            return {'This machine is unique on the trading platform'}
        average_cost_model_all = CurrencyService.calculate_average_cost(cars_this_model_all)
        cars_this_model_region = (cars_this_model_all.filter(region=car_serializer.data.get('region')))
        cars_this_model_region_serializer = CarSerializer(cars_this_model_region, many=True)
        if not cars_this_model_region_serializer.data:
            context = {'average_cost_model_Ukraine': average_cost_model_all,
                       'average_cost_model_region': 'This machine is unique in you region'}
            return context
        average_cost_model_region = CurrencyService.calculate_average_cost(cars_this_model_region)
        context = {'average_cost_model_Ukraine': average_cost_model_all,
                   'average_cost_model_region': average_cost_model_region}
        return context

