from django.urls import include, path

from .views import (TestEmailView, UserAddAvatarView, UserBlockView,
                    UserListCreateView, UserUnBlockView)

urlpatterns = [
    path('', UserListCreateView.as_view()),
    path('/<int:pk>/block', UserBlockView.as_view()),
    path('/<int:pk>/unblock', UserUnBlockView.as_view()),
    path('/<int:pk>/cars', UsersAddCarView.as_view(), name='users_add_car'),
    path('/avatars', UserAddAvatarView.as_view()),
    path('/test', TestEmailView.as_view())
]