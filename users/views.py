# Create your views here.

from django.db.models import Q
from rest_framework import generics, status, permissions
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import User
from .serializers import UserSerializer


class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny,)  # Allow any user to access

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({"message": "User created successfully"}, status=status.HTTP_201_CREATED)


class UserLoginView(TokenObtainPairView):
    permission_classes = (permissions.AllowAny,)  # Allow any user to access

    # No need to override post() method.
    # TokenObtainPairView handles token generation and response.


class UserSearchView(generics.ListAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        query = self.request.query_params.get('query')
        print(query)
        if query:
            return User.objects.filter(Q(email__iexact=query) | Q(name__icontains=query))
        return User.objects.none()  # Return empty queryset if no query is provided
