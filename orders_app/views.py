from django.shortcuts import render
from orders_app.forms import OrderForm
from django.http import HttpResponseRedirect
from orders_app.models import Order
from user_app.models import User
from django.contrib import messages


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
            print('форма валидна')
            form.save()
            messages.success(request, 'Заказ оформлен', extra_tags='success')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            print('форма не валидна')
            print(form.errors)
            messages.error(request, 'Ошибка при оформлении заказа!', extra_tags='danger')
        # if form.is_valid():
        #     form.save()
        #     messages.success(request, 'Заказ оформлен', extra_tags='success')
    return render(request, 'orders_app/order-create.html', context=context)
