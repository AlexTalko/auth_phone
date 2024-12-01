from django.test import TestCase

from users.models import User


class UserInterfaceTest(TestCase):
    """Тестирование интерфейса пользователя"""

    def test_login_page(self):
        """Проверяем открытие страницы входа"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def setUp(self):
        self.user = User.objects.create(phone='79991234567',
                                        invite_code='03m21C',
                                        first_name='Pest',
                                        country='United')
        self.user1 = User.objects.create(phone='79991234568',
                                         invite_code='03m21R',
                                         first_name='Test', )

    def test_user_create(self):
        """Проверяем создание пользователя"""
        self.assertEqual(User.objects.count(), 2)
        self.assertEqual(self.user.phone, '79991234567')
        self.assertEqual(self.user.invite_code, '03m21C')
        self.assertEqual(self.user.first_name, 'Pest')
        self.assertEqual(self.user.country, 'United')
        self.assertEqual(self.user1.phone, '79991234568')
        self.assertEqual(self.user1.invite_code, '03m21R')
        self.assertEqual(self.user1.first_name, 'Test')
