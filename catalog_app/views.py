from django.shortcuts import render, get_list_or_404
from catalog_app.models import Category, Product
from django.core.paginator import Paginator


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
    }
    return render(request, 'catalog_app/menu.html', context=context)
