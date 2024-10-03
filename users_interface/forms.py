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

    def clean_ref_code(self):
        """Проверяем ref_code"""

        ref_code = self.cleaned_data.get('ref_code')
        if ref_code:
            if ref_code == self.instance.invite_code:
                raise forms.ValidationError('Вы не можете использовать свой же код!')
            if not User.objects.filter(invite_code=ref_code).exists():
                raise forms.ValidationError('Пригласительный код не найден!')
            # if User.objects.filter(ref_code=ref_code).exists():
            #     raise forms.ValidationError('Уже использован код')
        return ref_code

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'country', 'ref_code',)
