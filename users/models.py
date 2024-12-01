from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models

from users.validators import phone_validator

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser, PermissionsMixin):
    username = None

    phone = models.CharField(max_length=16, unique=True, verbose_name='Телефон',
                             help_text='Укажите номер телефона в формате 79991233221', validators=[phone_validator])

    first_name = models.CharField(max_length=20, **NULLABLE, verbose_name='Имя')

    last_name = models.CharField(max_length=20, **NULLABLE, verbose_name='Фамилия')

    country = models.CharField(max_length=100, **NULLABLE, verbose_name='Страна', help_text='Откуда Вы?')

    invite_code = models.TextField(max_length=10, verbose_name='Код для приглашений', default=0)
    ref_code = models.TextField(max_length=10, verbose_name='использован пригласительный код', **NULLABLE)

    def get_reference(self):
        user_list = User.objects.filter(ref_code=self.invite_code)
        return [user.phone for user in user_list]

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.phone
