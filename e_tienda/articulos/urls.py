from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from articulos import views

urlpatterns = [
    path('', views.catalogo_articulos, name='catalogo_articulos'),
    path('articulos', views.lista_articulos, name='lista_articulos'),
    path('agregar', views.agregar_articulo, name='agregar_articulo'),
    path('editar/<int:id>', views.editar_articulo, name='editar_articulo'),
    path('eliminar/<int:id>', views.eliminar_articulo, name='eliminar_articulo'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    
