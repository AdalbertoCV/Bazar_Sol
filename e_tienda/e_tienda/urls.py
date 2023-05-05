from django.contrib import admin
from django.urls import path, include
from tienda.views import Bienvenida

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Bienvenida.as_view(), name="home"),
    path('usuarios/', include('usuarios.urls')),
]
