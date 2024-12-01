
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
    payment = serializers.IntegerField(validators=[V.MinValueValidator(300,
                                                                       message="Payment should be exactly 300."),
                                                   V.MaxValueValidator(300,
                                                                       message="Payment should be exactly 300.")])
    email = serializers.EmailField()


class SuccessSerializer(serializers.Serializer):
    details = serializers.CharField()


class TokenSerializer(serializers.Serializer):
    token = serializers.CharField()