from django.urls import path
from carts_app.views import add_to_carts, remove_from_carts, user_carts

app_name = 'carts_app'

urlpatterns = [
    path('add_to_carts/<slug:slug>/', add_to_carts, name='add_to_carts'),
    path('user_carts/', user_carts, name='user_carts'),
    path('remove_from_carts/<int:cart_id>/', remove_from_carts, name='remove_from_carts'),
]
