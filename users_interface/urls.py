from django.contrib.auth.views import LoginView
from django.urls import path


from users_interface.views import UserCreateView, SmsCodeView, ProfileView
from users_interface.apps import UsersInterfaceConfig

app_name = UsersInterfaceConfig.name

urlpatterns = [
    path('', UserCreateView.as_view(), name='login'),
    path('sms_code', SmsCodeView.as_view(), name='sms_code'),
    path('profile', ProfileView.as_view(), name='profile'),
]
