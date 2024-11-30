from django.urls import path

from .views import TradingPlatformInformationView, UserCarInformationView

urlpatterns = [
    path('', TradingPlatformInformationView.as_view()),
    path('/car/<int:pk>', UserCarInformationView.as_view()),
]