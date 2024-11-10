import os

from apps.cars.models import CurrencyModel
from apps.cars.serializers import CurrencySerializer
from configs.celery import app
from core.dataclasses.car_dataclass import CarDataClass
from core.dataclasses.user_dataclass import UserDataClass
from django.contrib.auth import get_user_model

UserModel = get_user_model()

list_of_profanity = ['Car', 'попа']

class NoProfanityService:
    @staticmethod
    def no_profanity_check(user, data):

        if any(sub in dict(data).get('information')[0] for sub in list_of_profanity):
            print(sub)
        else:
            return data
