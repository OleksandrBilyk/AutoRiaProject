from datetime import datetime

from core.enums.regex_enum import RegexEnum
from core.models import BaseModel
from core.services.upload_photo_car import upload_photo_car
from django.core import validators as V
from django.db import models

from apps.cars.choices import CarBrandChoices
from apps.users.models import UserModel


class CarModel(BaseModel):
    class Meta:
        db_table = 'cars'
        ordering = ('id',)

    brand = models.CharField(max_length=50, choices=[*CarBrandChoices.choices])
    price = models.IntegerField(validators=[V.MinValueValidator(0), V.MaxValueValidator(1000000)])
    year = models.IntegerField(validators=[V.MinValueValidator(1990), V.MaxValueValidator(datetime.now().year)])
    car_model = models.CharField(max_length=50, validators=[V.RegexValidator(*RegexEnum.MODEL_CAR.value)])
    photo_car = models.ImageField(upload_to=upload_photo_car)
    information = models.CharField(max_length=350, validators=[V.RegexValidator(*RegexEnum.INFORMATION.value)])
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='cars')
