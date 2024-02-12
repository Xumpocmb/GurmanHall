from django.shortcuts import render
from catalog_app.models import Category
from django.contrib import auth, messages


def index(request):
    context = {
        'title': 'Гурман Хол',
        'categories': Category.objects.all(),
    }
    return render(request, 'shop_app/index.html', context=context)


def contacts(request):
    context = {
        'title': 'Контакты',
    }
    if request.method == 'POST':
        name = request.POST.get('first_name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(name, email, message)
        messages.success(request, 'Сообщение отправлено!', extra_tags='success')
    return render(request, 'shop_app/contacts.html', context=context)
