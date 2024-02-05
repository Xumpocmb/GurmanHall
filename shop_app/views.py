from django.shortcuts import render
from catalog_app.models import Category


def index(request):
    context = {
        'title': 'Гурман Хол',
        'categories': Category.objects.all(),
    }
    return render(request, 'shop_app/index.html', context=context)
