from django.urls import path
from orders_app.views import order, orders, order_create

app_name = 'orders_app'

urlpatterns = [
    path('order/', order, name='order'),
    path('orders/', orders, name='orders'),
    path('order-create/', order_create, name='order_create'),
]
