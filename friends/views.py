# Create your views here.
# friends/views.py
from django.db import transaction
from django.db.models import Q
from rest_framework import generics, status
from rest_framework.exceptions import Throttled, ValidationError, PermissionDenied
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from users.serializers import UserSerializer
from .models import FriendRequest, User
from .serializers import FriendRequestSerializer
from .throttling import SendFriendRequestRateThrottle


class FriendRequestView(generics.CreateAPIView, generics.ListAPIView):
    serializer_class = FriendRequestSerializer
    throttle_classes = [SendFriendRequestRateThrottle]

    def create(self, request, *args, **kwargs):
        try:
            receiver_email = request.data.get('receiver_email')
            if not receiver_email:
                raise ValidationError({"receiver_email": "This field is required."})

            receiver = get_object_or_404(User, email=receiver_email)
            self.check_self_request(request.user, receiver)
            self.check_existing_friend_requests(request.user, receiver)
            self.check_existing_friends(request.user, receiver)

            friend_request = FriendRequest.objects.create(sender=request.user, receiver=receiver)
            serializer = self.get_serializer(friend_request)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Throttled as e:
            # Call handle_throttled to handle rate limit errors
            return self.handle_throttled(request, e.wait)

    @staticmethod
    def check_self_request(sender, receiver):
        if sender == receiver:
            raise ValidationError({"error": "You cannot send a friend request to yourself"})

    @staticmethod
    def check_existing_friend_requests(sender, receiver):
        if FriendRequest.objects.filter(
                Q(sender=sender, receiver=receiver, status='pending') |
                Q(sender=receiver, receiver=sender, status='pending')
        ).exists():
            raise ValidationError({"error": "Friend request already sent."})

    @staticmethod
    def check_existing_friends(sender, receiver):
        if FriendRequest.objects.filter(
                Q(sender=sender, receiver=receiver, status='accepted') |
                Q(sender=receiver, receiver=sender, status='accepted')
        ).exists():
            raise ValidationError({"error": "Both are already friends."})

    def handle_throttled(self, request, wait):
        # Customize throttled response, if needed
        raise Throttled(detail={"error": "Rate limit exceeded. Please try again later."}, wait=wait)

    def get_queryset(self):
        return self.request.user.received_requests.filter(status='pending')


class AcceptRejectFriendRequestView(generics.UpdateAPIView):
    serializer_class = FriendRequestSerializer

    def get_object(self):
        request_id = self.kwargs['request_id']
        obj = get_object_or_404(FriendRequest, pk=request_id, status='pending')
        self.check_object_permissions(self.request, obj)
        return obj

    @transaction.atomic()
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        _status = request.data.get('status')
        if _status not in ['accepted', 'rejected']:
            return Response({"error": "Invalid status"}, status=status.HTTP_400_BAD_REQUEST)
        instance.status = _status
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def check_object_permissions(self, request, obj):
        if request.user != obj.receiver:
            raise PermissionDenied(detail={"error": "You do not have permission to accept friend request."})


class ListFriendsView(generics.ListAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        friends = User.objects.filter(
            Q(sent_requests__receiver=self.request.user, sent_requests__status='accepted') |
            Q(received_requests__sender=self.request.user, received_requests__status='accepted')
        ).distinct()
        return friends
