from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    """Создание суперпользователя"""

    def handle(self, *args, **options):
        user = User.objects.create(phone='72223334455', invite_code='I82ib9')
        user.set_password('123456')
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save()
