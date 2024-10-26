from django.db.models import TextChoices


class CurrencyChoices(TextChoices):
    UAH = "UAH"
    USD = "USD"
    EUR = "EUR"


class CarBrandChoices(TextChoices):
    BMW = "BMW"
    AUDI = "AUDI"
    Fiat = 'Fiat'
    Mazda = 'Mazda'
    Nissan = 'Nissan'
    Scoda = 'Scoda'

