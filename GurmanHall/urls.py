from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('shop_app.urls', namespace='shop_app')),
    path('', include('catalog_app.urls', namespace='catalog_app')),

]

if settings.DEBUG:
    # подключаем media для отладки
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # urlpatterns += path("__debug__/", include("debug_toolbar.urls")),

