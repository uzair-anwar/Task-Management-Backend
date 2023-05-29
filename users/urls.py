from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework import routers

from .views import RegisterUserView, LoginUserView
from .views import CustomTokenObtainPairView
from .views import UserViewSet

router = routers.DefaultRouter()
router.register(r'managers', UserViewSet, basename='managers')
router.register(r'users', UserViewSet, basename='users')

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include(router.urls)),
]
