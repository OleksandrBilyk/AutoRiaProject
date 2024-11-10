import os

import requests
from apps.cars.models import CurrencyModel
from apps.cars.serializers import CurrencySerializer
from configs.celery import app
from core.dataclasses.user_dataclass import UserDataClass
from core.services.jwt_service import ActivateToken, JWTService, RecoveryToken
from django.contrib.auth import get_user_model
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template

UserModel = get_user_model()

class EmailService:
    @staticmethod
    @app.task
    def __send_email(to: str, template_name: str, context: dict, subject='') -> None:
        template = get_template(template_name)
        html_context = template.render(context)
        msg = EmailMultiAlternatives(subject, from_email=os.environ.get('EMAIL_HOST_USER'), to=[to])
        msg.attach_alternative(html_context, 'text/html')
        msg.send()

    @classmethod
    def register(cls, user:UserDataClass):
        token = JWTService.create_token(user, ActivateToken)
        url = f'http://localhost:80/api/auth/activate/{token}'
        cls.__send_email.delay(
            user.email, 'register.html',
            {'name':user.profile.name, 'url':url },
            'Register'
        )

    @classmethod
    def recovery_password(cls, user:UserDataClass):
        token = JWTService.create_token(user, RecoveryToken)
        url = f'http://localhost:80/api/auth/recovery/{token}'
        cls.__send_email.delay(
            user.email,
            'recovery.html', {'url': url},
            'Recovery password'
        )

    @classmethod
    def user_banned(cls, user: UserDataClass):
        for admin in UserModel.objects.filter(is_staff=True):
            cls.__send_email.delay(
                admin.email,
                'user_banned.html', {'admin_name':admin.profile.name,'name':user.email},
                'User banned due to profanity'
            )


    @classmethod
    def payment(cls, user: UserDataClass):
        url = f'http://localhost:80/api/auth/payment/'
        cls.__send_email.delay(
            user.email,
            'payment.html', {'url': url},
            'Payment for premium'
        )

    @staticmethod
    @app.task
    def get_currency():
        url = 'https://api.privatbank.ua/p24api/pubinfo?exchange&json&coursid=11'

        response = requests.get(url)

        if response.status_code == 200:
            currency = response.json()
            CurrencyModel.objects.all().delete()
            for data in currency:
                serializer = CurrencySerializer(data=data)
                serializer.is_valid(raise_exception=True)
                serializer.save()
        else:
            print(f'Request failed with status {response.status_code}')