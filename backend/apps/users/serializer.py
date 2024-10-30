from core.services.email_service import EmailService
from django.contrib.auth import get_user_model
from django.core.files import File
from django.db.transaction import atomic
from rest_framework import serializers

from apps.cars.serializers import CarSerializer
from apps.users.models import ProfileModel

UserModel = get_user_model()

class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProfileModel
        fields = ('id', 'name', 'surname', 'age', 'avatar', 'phone_number')


class ProfileAvatarSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileModel
        fields = ('avatar',)
        extra_kwargs = {'avatar': {'required': True}}

    def validate_avatar(self, avatar: File):
        max_size = 100 * 1024
        if avatar.size > max_size:
            raise serializers.ValidationError('max_size 100kb')
        return avatar

class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()
    cars = CarSerializer(many=True, read_only=True)
    class Meta:
        model = UserModel
        fields = (
            'id', 'email', 'password', 'is_active', 'is_staff', 'is_superuser', 'is_premium', 'last_login', 'created_at',
            'updated_at', 'profile', 'cars'
        )
        read_only_fields = ('id', 'is_active', 'is_staff', 'is_superuser', 'is_premium', 'last_login', 'created_at',
                            'updated_at', 'cars')
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }

    @atomic
    def create(self, validated_data:dict):
        profile = validated_data.pop('profile')
        user = UserModel.objects.create_user(**validated_data)
        ProfileModel.objects.create(**profile, user=user)
        EmailService.register(user)
        return user
