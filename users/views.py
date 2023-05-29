from rest_framework import viewsets
from django.contrib.auth import get_user_model
from rest_framework import generics, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import CustomTokenObtainPairSerializer
from .serializers import CustomUserSerializer


class RegisterUserView(generics.CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.AllowAny]


class LoginUserView(TokenObtainPairView):
    serializer_class = CustomUserSerializer


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.user.role == 'admin':
            return get_user_model().objects.filter(role='manager')
        if self.request.user.role == 'manager':
            return get_user_model().objects.filter(role='regular')
        else:
            return get_user_model().objects.none()

    def get_serializer_class(self):
        return CustomUserSerializer
