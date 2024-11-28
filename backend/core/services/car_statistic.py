
from datetime import date, datetime

from apps.cars.models import CarModel
from apps.cars.serializers import CarSerializer
from apps.information.models import CarViewingModel
from core.services.currency_service import CurrencyService
from rest_framework.generics import get_object_or_404


class CarStatisticService:
    @staticmethod
    def car_viewing_count(data):
        car_viewing = CarViewingModel.objects.filter(car_id=data.get('id'))
        car_viewing_all_time = car_viewing.count()
        car_viewing_by_day = car_viewing.filter(created_at__day=data.get('day')) if data.get('day') \
            else car_viewing.filter(created_at__day=date.today().day)
        car_viewing_by_month = car_viewing.filter(created_at__month=data.get('month')) if data.get('month') \
            else car_viewing.filter(created_at__month=date.today().month)
        car_viewing_by_week = car_viewing.filter(created_at__week=data.get('week')) if data.get('week') \
            else car_viewing.filter(created_at__week=datetime.now().isocalendar().week)
        context = {'car_viewing_all_time': car_viewing_all_time,
                   'car_viewing_by_month': car_viewing_by_month.count(),
                   'car_viewing_by_week,': car_viewing_by_week.count(),
                   'car_viewing_by_day': car_viewing_by_day.count()}
        return context
    @staticmethod
    def car_price_statistic(data):
        car = get_object_or_404(CarModel, id=data.get('id'))
        car_serializer = CarSerializer(car)
        cars_this_model_all = (CarModel.objects.exclude(id=data.get('id')).
                               filter(car_model=car_serializer.data.get('car_model')))
        cars_this_model_all_serializer = CarSerializer(cars_this_model_all, many=True)
        sum_of_price = {'UAH': 0, 'USD': 0, 'EUR': 0}
        for one_car in cars_this_model_all_serializer.data:
            one_car_full_price = CurrencyService.add_currency_to_car(one_car)
            sum_of_price['UAH'] += one_car_full_price['full_price']['UAH']
            sum_of_price['USD'] += one_car_full_price['full_price']['USD']
            sum_of_price['EUR'] += one_car_full_price['full_price']['EUR']
        print(sum_of_price)
        cars_this_model_region = (cars_this_model_all.filter(region=car_serializer.data.get('region')))

        # print(cars_serializer.data)


        # context = {'car_viewing_all_time': car_viewing_all_time,
        #            'car_viewing_by_month': car_viewing_by_month.count(),
        #            'car_viewing_by_week,': car_viewing_by_week.count(),
        #            'car_viewing_by_day': car_viewing_by_day.count()}
        return

