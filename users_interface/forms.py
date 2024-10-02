from django.forms import ModelForm, Form, CharField

from users.models import User


class UserRegisterForm(ModelForm):
    class Meta:
        model = User
        fields = ('phone',)


class SmsCode(Form):
    code = CharField(label='Код из SMS')

