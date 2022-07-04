from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from urllib.parse import urlparse
from urllib.parse import parse_qs

from .models import UserModel


def login_page(request):
    context = {
        'title': 'Вхід',
    }

    if request.method == 'POST':
        username = request.POST.get('Login')
        password = request.POST.get('Password')
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            return redirect('account', username=username)
        else:
            context['error'] = 'Невірний логін чи пароль'

    return render(request, 'accounts/login.html', context)


def logout_page(request):
    logout(request)
    return redirect('home')


def verify_page(request):
    url = request.build_absolute_uri()

    parsed_url = urlparse(url)
    login_user = parse_qs(parsed_url.query)['login'][0]
    password_user = parse_qs(parsed_url.query)['password'][0]

    if not User.objects.filter(username=login_user).exists():
        user = User.objects.create_user(
            username=login_user,
            password=password_user
        )
        user.save()

        user_auth = authenticate(request, username=login_user, password=password_user)

        if user_auth is not None and user_auth.is_active:
            login(request, user_auth)
            return redirect('account', username=login_user)
    else:
        user = authenticate(request, username=login_user, password=password_user)

        if user is not None and user.is_active:
            login(request, user)
            return redirect('account', username=login_user)


def account_page(request, username):

    user_tg = UserModel.objects.get(username=username)

    context = {
        'title': 'Обліковий запис',
        'username': username,
        'user_tg': user_tg,
        'admins': User.objects.filter(is_superuser=True),
    }
    return render(request, 'accounts/account.html', context)


def register_page(request):
    link = 'https://t.me/register_account_test_bot?start=%s' % 'register_user'
    return redirect(link)
