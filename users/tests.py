from rest_framework.test import APITestCase

from users.models import User
from users.services import generate_code


class UserTest(APITestCase):
    """Тестирование регистрации пользователя"""

    def setUp(self):
        self.user = User.objects.create(phone='79991234567', invite_code='03m21C', first_name='Pest', country='United')
        self.user1 = User.objects.create(phone='79991234568', invite_code='03m21R', ref_code='03m21C')

    def test_user_create(self):
        """Проверяем создание пользователя"""
        self.assertEqual(User.objects.count(), 2)
        self.assertEqual(self.user.phone, '79991234567')
        self.assertEqual(self.user1.phone, '79991234568')
        self.assertEqual(self.user.invite_code, '03m21C')
        self.assertEqual(self.user.first_name, 'Pest')
        self.assertEqual(self.user.country, 'United')
        self.assertEqual(self.user1.invite_code, '03m21R')

    def test_user_update(self):
        """Проверяем обновление полей пользователя"""
        self.user.first_name = 'Test'
        self.user.last_name = 'Pestov'
        self.user.ref_code = '03m21C'
        self.user.country = 'US'
        self.user.save()
        self.assertEqual(self.user.first_name, 'Test')
        self.assertEqual(self.user.last_name, 'Pestov')
        self.assertEqual(self.user.get_reference(), ['79991234568', '79991234567'])
        self.assertEqual(self.user.ref_code, '03m21C')
        self.assertEqual(self.user.country, 'US')

    def test_generate_code(self):
        """Тестирование генерации кода авторизации"""
        code = generate_code()
        self.assertTrue(len(code) == 6)
        self.assertFalse(code.isdigit())
