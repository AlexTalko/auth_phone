from rest_framework import status, generics
from rest_framework.response import Response

from users.models import User
from users.serializers import UserSerializer, ProfileSerializer
from users.services import create_invite_code, generate_code, send


class UserCreateAPIView(generics.CreateAPIView):
    """Сохраняет пользователя при первом входе, присваивает invite_code, высылает код для входа"""
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        return_data = {}
        try:
            serializer.is_valid(raise_exception=True)
            user = serializer.save()
            user.invite_code = create_invite_code()
            return_data['invite_code'] = user.invite_code
        except Exception:
            user = User.objects.get(phone=request.data.get('phone'))
            return_data['invite_code'] = user.invite_code
        finally:
            password = generate_code()
            user.set_password(password)
            user.save()
            # send(int(user.phone), f'Ваш код авторизации: {password}' )

        return Response(return_data, status=status.HTTP_201_CREATED)


class UserUpdateAPIView(generics.UpdateAPIView):
    """Обновление данных пользователя"""
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_object(self, *args, **kwargs):
        return self.request.user


class UserProfileAPIView(generics.RetrieveAPIView):
    """Отображение данных пользователя"""
    queryset = User.objects.all()
    serializer_class = ProfileSerializer

    def get_object(self, *args, **kwargs):
        return self.request.user
