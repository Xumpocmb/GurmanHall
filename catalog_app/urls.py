from django.urls import path
from catalog_app.views import catalog, product, add_to_basket

app_name = 'catalog_app'

urlpatterns = [
    path('', catalog, name='catalog'),
    path('<slug:slug>/', catalog, name='catalog'),
    path('product/<slug:slug>/', product, name='product'),
    path('add_to_basket/<slug:slug>/', add_to_basket, name='add_to_basket'),
    path('not_found/', catalog, name='not_found'),
]
