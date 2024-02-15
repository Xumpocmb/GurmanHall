from django.shortcuts import render
from orders_app.forms import OrderForm, OperatorOrderForm
from django.http import HttpResponseRedirect
from orders_app.models import Order
from user_app.models import User
from django.contrib import messages
from django.urls import reverse
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync


def order(request, order_id):
    show_order = Order.objects.get(id=order_id)
    context = {
        'title': 'Заказ №' + str(order_id),
        'order': show_order,
    }
    return render(request, 'orders_app/order.html', context=context)


def orders(request):
    context = {
        'title': 'Мои заказы',
        'orders': Order.objects.filter(customer__username=request.user),
    }
    return render(request, 'orders_app/orders.html', context=context)


def order_create(request):
    context = {
        'title': 'Оформление заказа',
        'form': OrderForm(),
    }

    if request.method == 'POST':
        form = OrderForm(request.POST)
        form.instance.customer = User.objects.get(username=request.user)

        if form.is_valid():
            if form.instance.phone and form.instance.address:
                user_order = form.save()
                user_order.fill_basket_history()
                messages.success(request, 'Заказ оформлен', extra_tags='success')
                channel_layer = get_channel_layer()
                async_to_sync(channel_layer.group_send)(
                    'orders',
                    {
                        'type': 'order_create',
                        'order_id': user_order.id,
                    })
                return HttpResponseRedirect(reverse('orders_app:orders'))
            else:
                messages.error(request, 'Укажите ваш телефон и адрес для оформления заказа!',
                               extra_tags='danger')
        else:
            messages.error(request, 'Ошибка при оформлении заказа!', extra_tags='danger')
    return render(request, 'orders_app/order-create.html', context=context)


def operator_order_create(request):
    if request.method == 'POST':
        form = OperatorOrderForm(request.POST)
        form.instance.customer = User.objects.get(username=request.user)
        if form.is_valid():
            # статус подтвержден надо сразу сделать

            new_order = form.save()
            new_order.fill_basket_history()
            new_order.description = form.cleaned_data.get('description', None)
            new_order.status = Order.CONFIRMED
            new_order = form.save()
            messages.success(request, 'Заказ оформлен', extra_tags='success')
            channel_layer = get_channel_layer()
            async_to_sync(channel_layer.group_send)(
                'orders',
                {
                    'type': 'order_create',
                    'order_id': new_order.id,
                })
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            messages.error(request, 'Ошибка при оформлении заказа!', extra_tags='danger')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
