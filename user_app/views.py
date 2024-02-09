from django.shortcuts import render
from django.contrib import auth, messages
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse


def register(request):
    return render(request, 'user_app/register.html')


def login(request):
    return render(request, 'user_app/login.html')


def logout(request):
    auth.logout(request)
    messages.success(request, 'Вы вышли из аккаунта!')
    return HttpResponseRedirect(reverse('shop_app:index'))


def profile(request):
    return render(request, 'user_app/profile.html')
