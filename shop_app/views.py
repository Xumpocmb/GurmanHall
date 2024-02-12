from django.shortcuts import render
from catalog_app.models import Category
from django.contrib import auth, messages
from django.core.mail import send_mail
from django.conf import settings
from shop_app.forms import ContactMessagesForm
from shop_app.models import ContactMessages


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
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        ContactMessages.objects.create(name=name, email=email, phone=phone, message=message)
        send_mail(
            subject='Сообщение с сайта',
            message=f'Имя: {name}\nEmail: {email}\nТелефон: {phone}\nСообщение: {message}',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=['gurmanxol@gmail.com', 'x-xumpocmb@yandex.by', 'gurmanhol@yandex.by'],
        )
        messages.success(request, 'Сообщение отправлено!', extra_tags='success')
    else:
        form = ContactMessagesForm()
        context['form'] = form
    return render(request, 'shop_app/contacts.html', context=context)


def send_email(name, email, message):
    pass