from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import CreateView, DetailView, UpdateView
from rest_framework.reverse import reverse_lazy, reverse

from users.models import User
from users.services import create_invite_code, generate_code
from users_interface.forms import UserRegisterForm, SmsCode, UserUpdateForm


class UserCreateView(CreateView):
    """Сохранение пользователя при первом входе, отправка кода для входа, присваивание invite_code при первом входе"""
    template_name = 'users_interface/register.html'
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('users_interface:login')

    def get_success_url(self, ):
        return reverse_lazy('users_interface:sms_code') + '?phone=' + self.object.phone

    def form_valid(self, form, *args, **kwargs):
        return_data = {}

        form.is_valid()
        user = form.save()
        user.invite_code = create_invite_code()
        return_data['invite_code'] = user.invite_code

        password = generate_code()
        user.set_password(password)
        user.save()
        # send_sms(int(user.phone), password)
        messages.success(self.request, 'Отправили код в смс!')
        return super().form_valid(form)

    def form_invalid(self, form, *args, **kwargs):
        user = User.objects.get(phone=form.data.get('phone'))

        password = generate_code()
        user.set_password(password)
        user.save()
        # send_sms(int(user.phone), password)
        # messages.success(self.request, 'Отправили код в смс!')
        self.object = user
        return redirect(self.get_success_url())


class SmsCodeView(View):
    """Проверка кода из SMS и авторизация пользователя"""
    def post(self, *args, **kwargs):
        phone = self.request.POST.get('phone')
        code = self.request.POST.get('code')
        user = authenticate(self.request, username=phone, password=code)
        if user is not None:
            login(self.request, user)
            # Redirect to a success page.
            return redirect(reverse('users_interface:user_detail'))
        else:
            # Return an 'invalid login' error message.
            return redirect(reverse('users_interface:login'))

    def get(self, *args, **kwargs):
        form = SmsCode()
        return render(self.request, 'users_interface/sms_code.html', {'form': form})


class UserDetailView(DetailView):
    """Отображение данных пользователя"""
    model = User
    template_name = 'users_interface/user_detail.html'
    # form_class = ProfileUpdateForm

    def get_object(self, queryset=None):
        return self.request.user


class UserUpdateView(UpdateView):
    """Обновление данных пользователя"""
    model = User
    template_name = 'users_interface/user_form.html'
    form_class = UserUpdateForm
    success_url = reverse_lazy('users_interface:user_detail')

    def get_object(self, queryset=None):
        return self.request.user

    def get_success_url(self, ):
        return reverse_lazy('users_interface:user_detail') + '?phone=' + self.object.phone
