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
    Chevrolet = 'Chevrolet'
    Ford = 'Ford'
    Honda = 'Honda'
    Hyundai = 'Hyundai'
    KIA = 'KIA'
    Lexus = 'Lexus'
    Mercedes_Benz = 'Mercedes-Benz'
    Mitsubishi = 'Mitsubishi'
    Opel = 'Opel'
    Peugeot = 'Peugeot'
    Toyota = 'Toyota'
    Volvo = 'Volvo'
    Volkswagen = 'Volkswagen'
    Other = 'Other'



