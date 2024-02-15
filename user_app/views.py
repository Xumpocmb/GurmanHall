from django.contrib import auth
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from user_app.forms import UserLoginForm, UserRegistrationForm, UserProfileForm, PasswordChangeForm, EmailChangeForm
from user_app.models import User, EmailVerification


def register(request):
    context = {
        'title': 'Гурман Хол - Регистрация',
    }
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,
                             'Вы успешно зарегистрировались! Подтвердите регистрацию, перейдя по ссылке в письме.')
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
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('user_app:profile'))
            if user.is_archived:
                messages.error(request, 'Ваш аккаунт был удален.'
                                        'Если хотите восстановить аккаунт, напишите в поддержку.', extra_tags='danger')
                return HttpResponseRedirect(reverse('shop_app:contacts'))
        else:
            messages.error(request, 'Неправильные имя или пароль', extra_tags='danger')
    else:
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('user_app:profile'))
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
    if request.method == 'POST':
        form = UserProfileForm(data=request.POST, instance=request.user, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ваш профиль успешно обновлен!', extra_tags='success')
            return HttpResponseRedirect(reverse('user_app:profile'))
        else:
            messages.error(request, 'При обновлении профиля произошла ошибка!', extra_tags='danger')
    else:
        form = UserProfileForm(instance=request.user)
    context['form'] = form
    return render(request, 'user_app/profile.html', context=context)


def email_verification(request, email, code):
    context = {
        'title': 'Подтверждение почты',
    }
    user = User.objects.get(email=email)
    user_email_verification = EmailVerification.objects.filter(user=user, code=code)
    if user_email_verification.exists():
        user.verified_email = True
        user.save()
        messages.success(request, 'Ваша почта успешно подтверждена!', extra_tags='success')
        return render(request, 'user_app/email_verification.html', context=context)
    else:
        messages.error(request, 'Код подтверждения некорректен!', extra_tags='danger')
    return HttpResponseRedirect(reverse('user_app:login'))


@login_required
def change_password(request):
    context = {
        'title': 'Изменение пароля',
    }
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Обновляем сеанс пользователя, чтобы избежать выхода из системы
            messages.success(request, 'Ваш пароль был успешно изменен.', extra_tags='success')
            return HttpResponseRedirect(reverse('user_app:profile'))
        else:
            messages.error(request, 'Пожалуйста, исправьте ошибки в форме.', extra_tags='danger')
    else:
        form = PasswordChangeForm(request.user)
    context['form'] = form
    return render(request, 'user_app/change_password.html', context=context)


@login_required
def change_email(request):
    context = {
        'title': 'Изменение email',
    }
    if request.method == 'POST':
        form = EmailChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ваш email был успешно изменен.', extra_tags='success')
            return HttpResponseRedirect(reverse('user_app:profile'))
    else:
        form = EmailChangeForm(instance=request.user)
    context['form'] = form
    return render(request, 'user_app/change_email.html', context=context)


@login_required
def delete_account(request):
    if request.method == 'POST':
        current_user = User.objects.get(username=request.user)
        current_user.is_archived = True
        current_user.is_active = False
        current_user.save()
        auth.logout(request)
        messages.success(request, 'Ваш аккаунт был успешно удален.', extra_tags='success')
        return HttpResponseRedirect(reverse('shop_app:index'))
    else:
        return render(request, 'user_app/delete_account.html')
