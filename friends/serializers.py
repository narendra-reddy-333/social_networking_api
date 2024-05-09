from rest_framework import serializers
from .models import FriendRequest


class FriendRequestSerializer(serializers.ModelSerializer):
    sender = serializers.ReadOnlyField(source='sender.email')  # Show sender's email
    receiver = serializers.ReadOnlyField(source='receiver.email')  # Show receiver's email

    class Meta:
        model = FriendRequest
        fields = ('id', 'sender', 'receiver', 'status', 'created_at')
        read_only_fields = ('id', 'sender', 'receiver', 'created_at')  # Make these read-only
