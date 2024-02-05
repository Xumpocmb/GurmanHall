from django.shortcuts import render, get_list_or_404
from catalog_app.models import Category, Product


def catalog(request, slug=None):
    if slug:
        goods = get_list_or_404(Product.objects.filter(category__slug=slug))
    else:
        goods = None
    context = {
        'title': 'Каталог',
        'categories': Category.objects.all(),
        'goods': goods,
    }
    return render(request, 'catalog_app/menu.html', context=context)
