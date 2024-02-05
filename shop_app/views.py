from django.shortcuts import render


def index(request):
    context = {
        'title': 'Гурман Хол - Готовим изысканные роллы!',
    }
    return render(request, 'shop_app/index.html', context=context)

