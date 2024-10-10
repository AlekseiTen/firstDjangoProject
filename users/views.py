import random
import secrets
import string

from django.contrib.auth.forms import PasswordResetForm
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView

from config.settings import EMAIL_HOST_USER
from users.forms import UserRegisterForm
from users.models import User


class UserCreateView(CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy("users:login")

    def form_valid(self, form):
        """Метод для отправки ссылки на почту, для её подтверждения """
        user = form.save()
        user.is_active = False
        token = secrets.token_hex(16)
        user.token = token
        user.save()
        host = self.request.get_host()
        url = f'http://{host}/users/email-confirm/{token}/'
        send_mail(
            subject="Подтверждение почты",
            message=f"Привет, перейди по ссылке для подтверждения почты {url}",
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email]
        )
        return super().form_valid(form)


def email_verification(request, token):
    """ф-ция для верификации токена, и активации пользователя"""
    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.token = None
    user.save()
    return redirect(reverse("users:login"))


def generate_random_password(length=8):
    # Определяем возможные символы для пароля
    characters = string.ascii_letters + string.digits + string.punctuation
    # Создаем пустую строку для пароля
    password = ''
    # Генерируем пароль
    for i in range(length):
        random_char = random.choice(characters)  # Выбираем случайный символ
        password += random_char  # Добавляем его к паролю

    return password


def reset_password(request):
    if request.method == "POST":
        form = PasswordResetForm(request.POST)
    else:
        form = PasswordResetForm()
    return render(request, 'users/password_reset.html', {'form': form})
