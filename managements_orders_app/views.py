from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
import user_app.views
from orders_app.models import Order
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from django.utils import timezone
from user_app.models import User


def role_check(user):
    return user.role in [User.CHEF, User.OPERATOR, User.COURIER]


@login_required
@user_passes_test(role_check, login_url='/')
def orders(request):
    user = User.objects.get(username=request.user)
    if user.role == User.CHEF:
        orders_for_user = Order.objects.filter(status__in=[Order.CONFIRMED, Order.PROCESSING])
    elif user.role == User.OPERATOR:
        orders_for_user = Order.objects.filter(status__in=[Order.CREATED, Order.READY])
    elif user.role == User.COURIER:
        orders_for_user = Order.objects.filter(status=Order.ON_WAY)
    else:
        orders_for_user = Order.objects.all()
    context = {
        'title': 'Заказы',
        'orders': orders_for_user,
    }
    return render(request, 'managements_orders_app/orders.html', context=context)


def order(request, order_id):
    context = {
        'title': 'Заказ #' + str(order_id),
    }
    find_order = get_object_or_404(Order, id=order_id)
    context['order'] = find_order
    return render(request, 'managements_orders_app/order.html', context=context)


def order_create(request):
    return render(request, 'managements_orders_app/order_create.html')


def management(request):
    context = {
        'title': 'Управление заказами'
    }
    return render(request, 'managements_orders_app/orders.html', context=context)


def change_status(request, order_id, status):
    status = int(status)
    find_order = get_object_or_404(Order, id=order_id)
    if status not in dict(Order.STATUSES).keys():
        return HttpResponse("Invalid status", status=400)
    find_order.status = status
    find_order.save()
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        'orders',
        {
            'type': 'order_update',
            'order_id': find_order.id,
            'order_status_text': find_order.get_status_display(),
            'created_at': timezone.localtime(find_order.created_at).isoformat(),
            'total_sum': find_order.basket_history['total_sum'],
        }
    )
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))





