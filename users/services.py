import string
import secrets

from users.models import User


def create_invite_code():
    """Создаем уникальный инвайт код для реферальной системы"""
    invite_code = generate_code()

    while invite_code in [code.invite_code for code in User.objects.all()]:
        invite_code = generate_code()

    print(invite_code)
    return invite_code


def generate_code():
    alphabet = string.ascii_letters + string.digits
    while True:
        invite_code = ''.join(secrets.choice(alphabet) for i in range(10))
        if (any(c.islower() for c in invite_code)
                and any(c.isupper() for c in invite_code)
                and sum(c.isdigit() for c in invite_code) >= 3):
            break
    return invite_code
