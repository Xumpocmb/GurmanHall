from django.urls import path
from shop_app.views import index, contacts

app_name = 'shop_app'

urlpatterns = [
    path('', index, name='index'),
    path('contacts/', contacts, name='contacts'),
]
