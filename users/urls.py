from django.urls import path
from rest_framework.permissions import AllowAny
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from users.apps import UsersConfig
from users.views import UserCreateAPIView, UserUpdateAPIView, UserProfileAPIView

app_name = UsersConfig.name


urlpatterns = format_suffix_patterns([
    path('login/', UserCreateAPIView.as_view(), name='login'),
    path('update/', UserUpdateAPIView.as_view(), name='update'),
    path('profile/', UserProfileAPIView.as_view(), name='profile'),


    path('token/', TokenObtainPairView.as_view(permission_classes=(AllowAny,)), name='token'),
    path('token/refresh/', TokenRefreshView.as_view(permission_classes=(AllowAny,)), name='token_refresh'),
])
