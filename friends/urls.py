# friends/urls.py

from django.urls import path
from .views import FriendRequestView, AcceptRejectFriendRequestView, ListFriendsView

urlpatterns = [
    path('requests/', FriendRequestView.as_view(), name='friend-requests'),
    path('requests/<int:request_id>/', AcceptRejectFriendRequestView.as_view(), name='accept-reject-friend-request'),
    path('', ListFriendsView.as_view(), name='list-friends'),
]