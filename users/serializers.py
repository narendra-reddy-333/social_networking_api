from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  # Add password field

    class Meta:
        model = User
        fields = ('id', 'email', 'name', 'bio', 'password')
        extra_kwargs = {'email': {'required': True}, 'password': {'required': True}}

    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data['email'],
            name=validated_data.get('name', ''),  # Handle optional name field
            bio=validated_data.get('bio', ''),  # Handle optional bio field
        )
        user.set_password(validated_data['password'])  # Set password securely
        user.save()
        return user
