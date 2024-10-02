from django.contrib.auth.forms import UserChangeForm
from django.forms import ModelForm, Form, CharField, forms

from users.models import User


class UserRegisterForm(ModelForm):
    class Meta:
        model = User
        fields = ('phone',)


class SmsCode(Form):
    code = CharField(label='Код из SMS')


class UserUpdateForm(UserChangeForm):

    # def clean_ref_code(self):
    #     ref_code = self.cleaned_data['ref_code']
    #     if ref_code != 0:
    #         raise forms.ValidationError('Вы уже использовали код')
    #     return ref_code

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'country', 'ref_code', 'invite_code')
