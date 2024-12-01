from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from apps.auth.views import (PaymentForPremiumView, RecoveryPasswordView,
                             RecoveryRequestView, SocketView, UserActivateView)

urlpatterns = [
    path('', TokenObtainPairView.as_view(), name='auth_login'),
    path('/refresh', TokenRefreshView.as_view(), name='auth_refresh_token'),
    path('/activate/<str:token>', UserActivateView.as_view(), name='auth_activate'),
    path('/recovery', RecoveryRequestView.as_view(), name='auth_recovery_password_request'),
    path('/recovery/<str:token>', RecoveryPasswordView.as_view(), name='auth_recovery_password'),
    path('/socket', SocketView.as_view(), name='auth_socket_token'),
    path('/payment', PaymentForPremiumView.as_view(), name='auth_pay_premium')
]