from django.db.models import TextChoices


class CarChoices(TextChoices):
    Hatchback = "Hatchback"
    Sedan = "Sedan"
    Coupe = 'Coupe'
    Crossover = 'Crossover'
    Universal = 'Universal'


class CarBrandChoices(TextChoices):
    BMW = "BMW"
    AUDI = "AUDI"
    Fiat = 'Fiat'
    Mazda = 'Mazda'
    Nissan = 'Nissan'
    Scoda = 'Scoda'
