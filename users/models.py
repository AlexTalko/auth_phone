from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None
    objects = models.Manager()

    phone = models.CharField(max_length=16, unique=True, verbose_name='Телефон',
                             help_text='Укажите номер телефона в формате...', default=0)

    first_name = models.CharField(max_length=20, **NULLABLE, verbose_name='Имя')

    last_name = models.CharField(max_length=20, **NULLABLE, verbose_name='Фамилия')

    country = models.CharField(max_length=100, **NULLABLE, verbose_name='Страна', help_text='Откуда Вы?')

    invite_code = models.TextField(max_length=10, verbose_name='Код для приглашений', default=0)

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.phone
