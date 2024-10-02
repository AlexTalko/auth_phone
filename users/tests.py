from rest_framework.test import APITestCase

from users.models import User
from users.services import generate_code

# def test_generate_code():
#     """Тестирование генерации кода авторизации"""
#     code = generate_code()
#     code.assertEqual(len(code), 6)
#     code.assertTrue(code.isdigit())

class UserTest(APITestCase):
    """Тестирование регистрации пользователя"""

    def setUp(self):
        self.user = User.objects.create(phone='79991234567', invite_code='03m21C', first_name='Pest', country='United')
        # self.user = User.objects.create(phone='79991234568', invite_code='03m21R', ref_code='03m21C')


    def test_user_create(self):
        """Проверяем создание пользователя"""
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(self.user.phone, '79991234567')
        self.assertEqual(self.user.invite_code, '03m21C')
        self.assertEqual(self.user.first_name, 'Pest')
        self.assertEqual(self.user.country, 'United')
        # self.assertEqual(self.user.invite_code, '03m21C')

    def test_user_update(self):
        """Проверяем обновление полей пользователя"""
        self.user.first_name = 'Test'
        self.user.last_name = 'Pestov'
        self.user.ref_code = '03m21C'
        self.user.country = 'US'
        self.user.save()
        self.assertEqual(self.user.first_name, 'Test')
        self.assertEqual(self.user.last_name, 'Pestov')
        self.assertEqual(self.user.get_reference(), ['79991234567'])
        self.assertEqual(self.user.ref_code, '03m21C')
        self.assertEqual(self.user.country, 'US')


