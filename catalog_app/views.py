from django.core.paginator import Paginator
from django.shortcuts import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from django.http import JsonResponse
from django.utils.html import escape
from catalog_app.models import Category, Product
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


def add_to_basket(request, slug):
    # current_page = request.META.get('HTTP_REFERER')

    # count = request.GET.get('count')
    # if item.category.slug == 'zapechennyee-rolly':
    #     souce = request.GET.get('souse-option')
    # else:
    #     souce = 'Без соуса'
    # print(f'Продукт: {item.name} | Количество {count} | Соус для шапочки запеченных роллов: {souce if souce else "Шапочки нет"}')
    # messages.success(request, 'Товар добавлен!')
    # return HttpResponseRedirect(current_page)
    if request.method == 'POST':
        item = Product.objects.get(slug=slug)
        form_data = request.POST.get('form')
        decoded_data = urllib.parse.unquote(form_data)
        form_dict = dict(item.split('=') for item in decoded_data.split('&'))
        count = escape(int(form_dict.get('count')))
        souse_option = escape(form_dict.get('souse-option'))
        print(item.name, count, souse_option)
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})


def not_found(request):
    return render(request, '404.html')
