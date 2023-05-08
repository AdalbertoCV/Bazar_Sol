from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from tienda.views import Bienvenida
from  usuarios.views import LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LoginView.as_view(), name="login_home"),
    path('home/', Bienvenida.as_view(), name="home"),
    path('usuarios/', include('usuarios.urls')),
    path('articulos/', include('articulos.urls')),
    path('carrito/', include('carrito.urls')),
    path('reportes/', include('reportes.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
