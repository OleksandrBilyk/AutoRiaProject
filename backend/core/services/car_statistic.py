
from datetime import date, datetime

from apps.cars.models import CarModel
from apps.cars.serializers import CarSerializer
from apps.information.models import CarViewingModel
from rest_framework.generics import get_object_or_404


class CarStatisticService:
    @staticmethod
    def car_viewing_count(data):
        # car = get_object_or_404(CarModel, id=)
        # car_serializer = CarSerializer(car)
        car_viewing = CarViewingModel.objects.filter(car_id=data['id'])
        car_viewing_all_time = car_viewing.count()
        car_viewing_by_day = car_viewing.filter(created_at__day=data['day']) if data.get('day') \
            else car_viewing.filter(created_at__day=date.today().day)
        car_viewing_by_month = car_viewing.filter(created_at__month=data['month']) if data.get('month') \
            else car_viewing.filter(created_at__month=date.today().month)
        car_viewing_by_week = car_viewing.filter(created_at__week=data['week']) if data.get('week') \
            else car_viewing.filter(created_at__week=datetime.now().isocalendar().week)
        context = {'car_viewing_all_time': car_viewing_all_time,
                   'car_viewing_by_month': car_viewing_by_month.count(),
                   'car_viewing_by_week,': car_viewing_by_week.count(),
                   'car_viewing_by_day': car_viewing_by_day.count()}
        return context
    @staticmethod
    def car_price_statistic(data):
        # car = get_object_or_404(CarModel, id=)
        # car_serializer = CarSerializer(car)
        car_viewing = CarViewingModel.objects.filter(car_id=data['id'])
        car_viewing_all_time = car_viewing.count()
        car_viewing_by_day = car_viewing.filter(created_at__day=data['day']) if data.get('day') \
            else car_viewing.filter(created_at__day=date.today().day)
        car_viewing_by_month = car_viewing.filter(created_at__month=data['month']) if data.get('month') \
            else car_viewing.filter(created_at__month=date.today().month)
        car_viewing_by_week = car_viewing.filter(created_at__week=data['week']) if data.get('week') \
            else car_viewing.filter(created_at__week=datetime.now().isocalendar().week)
        context = {'car_viewing_all_time': car_viewing_all_time,
                   'car_viewing_by_month': car_viewing_by_month.count(),
                   'car_viewing_by_week,': car_viewing_by_week.count(),
                   'car_viewing_by_day': car_viewing_by_day.count()}
        return context
