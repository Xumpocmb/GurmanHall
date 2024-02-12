from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from django.http import JsonResponse
from django.utils.html import escape
from catalog_app.models import Category, Product
from carts_app.models import Basket
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





def not_found(request):
    return render(request, '404.html')
