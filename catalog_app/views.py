from django.shortcuts import render, get_list_or_404
from catalog_app.models import Category, Product


def catalog(request, slug=None):
    if slug:
        products = Product.objects.filter(category__slug=slug)
    else:
        products = Product.objects.all()
    context = {
        'title': 'Каталог',
        'categories': Category.objects.all(),
        'products': products,
    }
    return render(request, 'catalog_app/menu.html', context=context)
