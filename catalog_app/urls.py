from django.urls import path
from catalog_app.views import catalog

app_name = 'catalog_app'

urlpatterns = [
    path('', catalog, name='catalog'),
    path('<slug:slug>/', catalog, name='catalog'),
]
