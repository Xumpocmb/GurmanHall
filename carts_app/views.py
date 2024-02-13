import re

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponseRedirect
from django.shortcuts import render

from carts_app.models import Basket
from catalog_app.models import Product


@login_required(login_url='user_app:login')
def add_to_carts(request, slug):
    item = Product.objects.get(slug=slug)

    quantity_from_page = re.sub(r'\D', '', request.GET.get('count', 1))
    if quantity_from_page:
        quantity_from_page = int(quantity_from_page)
    else:
        messages.error(request, 'Ошибка: Необходимо ввести хотя бы одну цифру!', extra_tags='danger')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    sauce_from_page = request.GET.get('souse-option', None)

    if item.category.slug == 'zapechennyee-rolly':
        baskets = Basket.objects.filter(user=request.user, product=item, sauce=sauce_from_page)
        if not baskets.exists():
            Basket.objects.create(user=request.user, product=item, quantity=quantity_from_page, sauce=sauce_from_page)
        else:
            basket = baskets.first()
            basket.quantity += quantity_from_page
            basket.save()
    else:

        baskets = Basket.objects.filter(user=request.user, product=item)
        if not baskets.exists():
            Basket.objects.create(user=request.user, product=item, quantity=quantity_from_page)
        else:
            basket = baskets.first()
            basket.quantity += quantity_from_page
            basket.sauce = 'Без соуса'
            basket.save()
    messages.success(request, 'Товар добавлен!', extra_tags='success')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def remove_from_carts(request, cart_id):
    basket = Basket.objects.get(id=cart_id)
    basket.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def user_carts(request):
    context = {
        'title': 'Корзина'
    }
    return render(request, 'carts_app/cart.html', context=context)


def click_on_plus(request, cart_id):
    basket = Basket.objects.get(id=cart_id)
    basket.quantity += 1
    basket.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def click_on_minus(request, cart_id):
    basket = Basket.objects.get(id=cart_id)
    if basket.quantity > 1:
        basket.quantity -= 1
        basket.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
