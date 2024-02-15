from django.urls import path
from orders_app.views import order, orders, order_create, operator_order_create

app_name = 'orders_app'

urlpatterns = [
    path('order/<int:order_id>/', order, name='order'),
    path('orders/', orders, name='orders'),
    path('order-create/', order_create, name='order_create'),
    path('operator_order_create/', operator_order_create, name='operator_order_create'),
]
