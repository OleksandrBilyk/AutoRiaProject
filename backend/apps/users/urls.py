from django.urls import path

from .views import (UserAddAvatarView, UserBlockView, UserListCreateView,
                    UserUnBlockView)

urlpatterns = [
    path('', UserListCreateView.as_view()),
    path('/<int:pk>/block', UserBlockView.as_view()),
    path('/<int:pk>/unblock', UserUnBlockView.as_view()),
    path('/<int:pk>/avatars', UserAddAvatarView.as_view()),
]