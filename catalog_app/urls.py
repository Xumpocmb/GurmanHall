from django.urls import path
from catalog_app.views import catalog, product


app_name = 'catalog_app'

urlpatterns = [
    path('', catalog, name='catalog'),
    path('<slug:slug>/', catalog, name='catalog'),
    path('product/<slug:slug>/', product, name='product'),
    path('not_found/', catalog, name='not_found'),
]
