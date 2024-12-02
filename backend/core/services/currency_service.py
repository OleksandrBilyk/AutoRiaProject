
from apps.cars.models import CurrencyModel
from apps.cars.serializers import CarSerializer


class CurrencyService:
    """
    Service for car value transactions.
    """
    @staticmethod
    def add_currency_to_car(data):
        """
        a function that takes the cost of a car in any currency and converts the amount into three currencies.
        The conversion uses data obtained from the PrivatBank API
        """
        currency_data = CurrencyModel.objects.all()
        cross_course = {arg.ccy: (arg.buy, arg.sale) for arg in currency_data}
        data['cross_course'] = cross_course
        match data.get('currency'):
            case 'UAH':
                full_price = {'UAH': data.get('price'),
                              'USD': data.get('price') / float(cross_course.get('USD')[0]),
                              'EUR': data.get('price') / float(cross_course.get('EUR')[0])}
                data['full_price'] = full_price
            case 'USD':
                full_price = {'UAH': data.get('price') * float(cross_course.get('USD')[1]),
                              'USD': data.get('price'),
                              'EUR': (data.get('price') * float(cross_course.get('USD')[1])) / float(
                                  cross_course.get('EUR')[0])}
                data['full_price'] = full_price
            case 'EUR':
                full_price = {'UAH': data.get('price') * float(cross_course.get('EUR')[1]),
                              'USD': (data.get('price') * float(cross_course.get('EUR')[1])) / float(
                                  cross_course.get('USD')[0]),
                              'EUR': data.get('price')}
                data['full_price'] = full_price
        return data

    @staticmethod
    def calculate_average_cost(cars):
        """
        function that calculates the average price of cars in three currencies
        """
        cars_serializer = CarSerializer(cars, many=True)
        sum_of_price = {'UAH': 0, 'USD': 0, 'EUR': 0}
        for one_car in cars_serializer.data:
            one_car_full_price = CurrencyService.add_currency_to_car(one_car)
            sum_of_price['UAH'] += float(one_car_full_price['full_price']['UAH'])
            sum_of_price['USD'] += float(one_car_full_price['full_price']['USD'])
            sum_of_price['EUR'] += float(one_car_full_price['full_price']['EUR'])
        average_cost_model = {'UAH': sum_of_price.get('UAH') / cars.count(),
                              'USD': sum_of_price.get('USD') / cars.count(),
                              'EUR': sum_of_price.get('EUR') / cars.count()}
        return average_cost_model
