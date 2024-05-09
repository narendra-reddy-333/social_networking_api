from django.db.models import Q
from rest_framework import generics, status, permissions
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import User
from .serializers import UserSerializer


class UserRegistrationView(generics.CreateAPIView):
    """
    View for registering new users.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny,)  # Allow any user (even unauthenticated) to access

    def create(self, request, *args, **kwargs):
        """
        Handles user registration.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)  # Raise an exception if data is invalid
        user = serializer.save()  # Save the new user
        return Response({"message": "User created successfully"}, status=status.HTTP_201_CREATED)


class UserLoginView(TokenObtainPairView):
    """
    View for user login and JWT token generation.
    """
    permission_classes = (permissions.AllowAny,)  # Allow any user to access

    # No need to override post() method as TokenObtainPairView handles 
    # token generation and response based on credentials.


class UserSearchView(generics.ListAPIView):
    """
    View for searching users by email or name.
    """
    serializer_class = UserSerializer

    def get_queryset(self):
        """
        Filters users based on the provided query parameter.
        """
        query = self.request.query_params.get('query')
        if query:
            # Search for users with matching email (case-insensitive) or name containing the query
            return User.objects.filter(Q(email__iexact=query) | Q(name__icontains=query))
        return User.objects.none()  # Return an empty queryset if no query is provided
