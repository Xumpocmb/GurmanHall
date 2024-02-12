from carts_app.models import Basket


def baskets(request):
    return {'user_carts': Basket.objects.filter(user=request.user) if request.user.is_authenticated else []}
