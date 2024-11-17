
from apps.cars.models import CurrencyModel


class CurrencyService:
    @staticmethod
    def add_currency_to_car(data):
        currency_data = CurrencyModel.objects.all()
        cross_course = {arg.ccy: (arg.buy, arg.sale) for arg in currency_data}
        data['cross_course'] = cross_course
        match data.get('currency'):
            case 'UAH':
                full_price = {'UAH': data.get('price'),
                              'USD': data.get('price') / float(cross_course.get('USD')[0]),
                              'EUR': data.get('price') / float(cross_course.get('EUR')[0])},
                data['full_price'] = full_price
            case 'USD':
                full_price = {'UAH': data.get('price') * float(cross_course.get('USD')[1]),
                              'USD': data.get('price'),
                              'EUR': (data.get('price') * float(cross_course.get('USD')[1])) / float(
                                  cross_course.get('EUR')[0])},
                data['full_price'] = full_price
            case 'EUR':
                full_price = {'UAH': data.get('price') * float(cross_course.get('EUR')[1]),
                              'USD': (data.get('price') * float(cross_course.get('EUR')[1])) / float(
                                  cross_course.get('USD')[0]),
                              'EUR': data.get('price')},
                data['full_price'] = full_price
        return data
