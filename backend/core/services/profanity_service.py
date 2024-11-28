import os

from apps.users.serializer import UserSerializer
from core.services.email_service import EmailService
from django.contrib.auth import get_user_model

UserModel = get_user_model()

list_of_profanity = ['dick', 'жопа']  # This is a list of profanity words. In reality, it will be larger and expandable

class NoProfanityService:
    @staticmethod
    def no_profanity_check(user, data):
        if any(sub in dict(data).get('information')[0] for sub in list_of_profanity):
            user.is_active -= 1
            user.save()
            if user.is_active == 0:
                EmailService.user_banned(user)
                return 'User is not active, please send message to admin for unban'
            else: 
                return (f'In your ad, the system found obscene language, '
                        f'you have {user.is_active} attempts to change the ad')
        else:
            user.is_active = 3
            user.save()
            return True
