from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('shop_app.urls', namespace='shop_app')),
    path('catalog/', include('catalog_app.urls', namespace='catalog_app')),
    path('carts/', include('carts_app.urls', namespace='carts_app')),
    path('user/', include('user_app.urls', namespace='user_app')),
    path('orders/', include('orders_app.urls', namespace='orders_app')),

]

if settings.DEBUG:
    # подключаем media для отладки
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # urlpatterns += path("__debug__/", include("debug_toolbar.urls")),

