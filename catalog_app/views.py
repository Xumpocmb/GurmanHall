from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from django.http import JsonResponse
from django.utils.html import escape
from catalog_app.models import Category, Product, Basket
import urllib.parse


def catalog(request, slug=None):
    if slug:
        products = Product.objects.filter(category__slug=slug)
    else:
        products = Product.objects.all()

    page = int(request.GET.get('page', 1))
    paginator = Paginator(products, 6)
    current_page = paginator.page(page)

    context = {
        'title': 'Каталог',
        'categories': Category.objects.all(),
        'products': current_page,
        'nav_link': slug,
    }
    return render(request, 'catalog_app/menu.html', context=context)


def product(request, slug):
    item = Product.objects.get(slug=slug)
    context = {
        'product': item,
        'title': item.name,
    }
    return render(request, 'catalog_app/card.html', context=context)


@login_required(login_url='user_app:login')
def add_to_basket(request, slug):
    item = Product.objects.get(slug=slug)
    baskets = Basket.objects.filter(user=request.user, product=item)
    if not baskets.exists():
        Basket.objects.create(user=request.user, product=item, quantity=1)
    else:
        basket = baskets.first()
        basket.quantity += 1
        if item.category.slug == 'zapechennyee-rolly':
            basket.sauce = request.GET.get('souse-option')
        else:
            basket.sauce = 'Без соуса'
        basket.save()
    messages.success(request, 'Товар добавлен!')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def remove_from_basket(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def not_found(request):
    return render(request, '404.html')
