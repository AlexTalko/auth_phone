import string
import secrets

from users.models import User

from smsaero import SmsAero

from config.settings import SMSAERO_EMAIL, SMSAERO_API_KEY
from users.apps import UsersConfig

app_name = UsersConfig.name


def generate_code():
    """Создаем случайный код"""
    alphabet = string.ascii_letters + string.digits
    while True:
        random_code = ''.join(secrets.choice(alphabet) for i in range(6))
        if (any(c.islower() for c in random_code)
                and any(c.isupper() for c in random_code)
                and sum(c.isdigit() for c in random_code) >= 3):
            break
    print(random_code)
    return random_code


def create_invite_code():
    """Проверяем инвайт код на уникальность, для реферальной системы"""
    invite_code = generate_code()

    while invite_code in [code.invite_code for code in User.objects.all()]:
        invite_code = generate_code()

    return invite_code


def send(phone: int, message: str) -> dict:
    """phone (int): Номер телефона, на который будет отправлено SMS-сообщение.
    message (str): Содержимое SMS-сообщения, которое будет отправлено.
    """
    api = SmsAero(SMSAERO_EMAIL, SMSAERO_API_KEY)
    return api.send(phone, message)
