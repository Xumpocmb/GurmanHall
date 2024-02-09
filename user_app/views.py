from django.contrib import auth, messages
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from user_app.forms import UserLoginForm, UserRegistrationForm


def register(request):
    context = {
        'title': 'Гурман Хол - Регистрация',
    }
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно зарегистрировались!')
            return HttpResponseRedirect(reverse('user_app:login'))
    else:
        form = UserRegistrationForm()
    context['form'] = form
    return render(request, 'user_app/register.html', context)


def login(request):
    context = {
        'title': 'Гурман Хол - Авторизация',
    }
    if request.method == 'POST':
        print('request.POST')
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('user_app:profile'))
        else:
            messages.error(request, 'Неправильные имя или пароль')
    else:
        form = UserLoginForm()
    context['form'] = form
    return render(request, 'user_app/login.html', context)


@login_required(login_url='user_app:login')
def logout(request):
    auth.logout(request)
    messages.info(request, 'Вы вышли из аккаунта!')
    return HttpResponseRedirect(reverse('shop_app:index'))


@login_required(login_url='user_app:login')
def profile(request):
    username = request.user.username
    context = {
        'title': f'{username} -Профиль пользователя',
    }
    return render(request, 'user_app/profile.html', context=context)
