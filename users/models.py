from django.contrib.auth.models import AbstractUser
from django.forms import models


class User(AbstractUser):
    username = None

    phone = models.MobileField(max_length=)
