from django.urls import include, path

from .views import (UserAddAvatarView, UserBlockView, UserListCreateView,
                    UsersAddCarView, UserUnBlockView)

urlpatterns = [
    path('', UserListCreateView.as_view()),
    path('/<int:pk>/block', UserBlockView.as_view()),
    path('/<int:pk>/unblock', UserUnBlockView.as_view()),
    path('/<int:pk>/cars', UsersAddCarView.as_view()),
    path('/<int:pk>/avatars', UserAddAvatarView.as_view()),
]