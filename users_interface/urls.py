from django.urls import path


from users_interface.views import login
from users_interface.apps import UsersInterfaceConfig

app_name = UsersInterfaceConfig.name

urlpatterns = [
    path('', login, name='login'),
]
