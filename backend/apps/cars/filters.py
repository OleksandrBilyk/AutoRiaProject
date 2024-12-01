from django_filters import rest_framework as filters


class CarFilter(filters.FilterSet):
    year_lt = filters.NumberFilter('year','lt')
    year_gt = filters.NumberFilter('year','gt')
    price_lt = filters.NumberFilter('price','lt')
    price_gt = filters.NumberFilter('price','gt')
    region = filters.CharFilter('region', 'icontains')
    brand=filters.CharFilter('brand','icontains')
    car_model=filters.CharFilter('car_model','icontains')

    order = filters.OrderingFilter(
        fields=(
            'id',
            'price'
        )
    )