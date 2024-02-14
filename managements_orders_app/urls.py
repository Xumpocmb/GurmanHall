from django.urls import path
from managements_orders_app.views import order, orders, order_create, management, change_status

app_name = 'managements_orders_app'

urlpatterns = [
    path('', management, name='management'),
    path('order/<int:order_id>/', order, name='order'),
    path('orders/', orders, name='orders'),
    path('order-create/', order_create, name='order_create'),
    path('change-status/<int:order_id>/<str:status>/', change_status, name='change_status'),]