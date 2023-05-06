from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from tienda.views import Bienvenida

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Bienvenida.as_view(), name="home"),
    path('usuarios/', include('usuarios.urls')),
    path('articulos/', include('articulos.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
