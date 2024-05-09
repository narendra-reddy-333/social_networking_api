# social_network/urls.py or users/urls.py

from django.urls import path
from .views import UserRegistrationView, UserLoginView, UserSearchView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='user-register'),
    path('login/', UserLoginView.as_view(), name='user-login'),
    path('search/', UserSearchView.as_view(), name='user-search'),
]