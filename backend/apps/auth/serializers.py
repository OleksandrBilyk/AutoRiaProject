
from django.contrib.auth import get_user_model
from django.core import validators as V
from rest_framework import serializers

UserModel = get_user_model()


class EmailSerializer(serializers.Serializer):
    email = serializers.EmailField()


class PasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('password', )


class PaymentSerializer(serializers.Serializer):
    payment = serializers.IntegerField(validators=[V.MinValueValidator(300), V.MaxValueValidator(300)])
    email = serializers.EmailField()