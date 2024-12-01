from core.services.email_service import EmailService
from core.services.jwt_service import (ActivateToken, JWTService,
                                       RecoveryToken, SocketToken)
from django.contrib.auth import get_user_model
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.generics import GenericAPIView, get_object_or_404
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from apps.users.serializer import UserSerializer

from .serializers import (EmailSerializer, PasswordSerializer,
                          PaymentSerializer, SuccessSerializer,
                          TokenSerializer)

UserModel = get_user_model()


class UserActivateView(GenericAPIView):
    """
    Activate user account
    """
    permission_classes = [AllowAny]

    def get_serializer(self, *args, **kwargs):
        pass

    @swagger_auto_schema(operation_id='Activate user', responses={status.HTTP_200_OK: UserSerializer}, security=[])
    def post(self, *args, **kwargs):
        token = kwargs['token']
        user = JWTService.validate_token(token, ActivateToken)
        user.is_active = 3
        user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data, status.HTTP_200_OK)


class RecoveryRequestView(GenericAPIView):
    """
        Send email to recovery password
    """
    permission_classes = (AllowAny,)
    serializer_class = EmailSerializer

    @swagger_auto_schema(operation_id='Request to recovery password',
                         responses={status.HTTP_200_OK: SuccessSerializer}, security=[])
    def post(self, *args, **kwargs):
        data = self.request.data
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        user = get_object_or_404(UserModel, **serializer.data)
        EmailService.recovery_password(user)
        return Response({'detail':'check your email'}, status.HTTP_200_OK)


class RecoveryPasswordView(GenericAPIView):
    """
            Send new password and token received for recovery
    """
    permission_classes = (AllowAny,)
    serializer_class = PasswordSerializer

    @swagger_auto_schema(operation_id='Set new user password', request={PasswordSerializer},
                         responses={status.HTTP_200_OK: SuccessSerializer}, security=[])
    def post(self, *args, **kwargs):
        data = self.request.data
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        token = kwargs['token']
        user = JWTService.validate_token(token, RecoveryToken)
        user.set_password(serializer.data['password'])
        user.save()
        return Response({'detail': 'password changed'}, status.HTTP_200_OK)


class PaymentForPremiumView(GenericAPIView):
    """
    Payment page for premium status for the user. You need to enter exactly 300, and user's email
    """
    permission_classes = (AllowAny,)
    serializer_class = PaymentSerializer

    @swagger_auto_schema(operation_id='Payment premium user', responses={status.HTTP_200_OK: UserSerializer}, security=[])
    def post(self, *args, **kwargs):
        data = self.request.data
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        user = get_object_or_404(UserModel, email=serializer.data.get('email'))
        user.is_premium = True
        user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data, status.HTTP_200_OK)


class SocketView(GenericAPIView):
    """
                Get socket token
    """
    permission_classes = (IsAuthenticated,)

    @swagger_auto_schema(responses={status.HTTP_200_OK: TokenSerializer})
    def get(self, *args, **kwargs):
        token = JWTService.create_token(self.request.user, SocketToken)
        return Response({'token': str(token)}, status.HTTP_200_OK)


