from django.shortcuts import render
from orders_app.forms import OrderForm
from django.http import HttpResponseRedirect
from orders_app.models import Order
from user_app.models import User
from django.contrib import messages
from django.urls import reverse


def order(request):
    return render(request, 'orders_app/order.html')


def orders(request):
    return render(request, 'orders_app/orders.html')


def order_create(request):
    context = {
        'title': 'Оформление заказа',
        'form': OrderForm(),
    }

    if request.method == 'POST':
        form = OrderForm(request.POST)
        form.instance.customer = User.objects.get(username=request.user)

        if form.is_valid():
            user = form.instance.customer
            if user.phone and user.address:
                user_order = form.save()
                user_order.fill_basket_history()
                messages.success(request, 'Заказ оформлен', extra_tags='success')
                return HttpResponseRedirect(reverse('orders_app:orders'))
            else:
                messages.error(request, 'Укажите ваш телефон и адрес для оформления заказа!',
                               extra_tags='danger')
        else:
            messages.error(request, 'Ошибка при оформлении заказа!', extra_tags='danger')
    return render(request, 'orders_app/order-create.html', context=context)
