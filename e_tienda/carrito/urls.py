from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from carrito import views

urlpatterns = [
    path('<int:id>', views.VerCarrito, name='ver_carrito'),
    path('agregar_al_carrito/<int:id>/<int:id_carrito>', views.AgregarAlCarrito, name='agregar_al_carrito'),
    path('vaciar_carrito/<int:id>', views.vaciarCarrito, name='vaciar_carrito'),
    path('comprar_carrito/<int:id>', views.comprarCarrito, name='comprar_carrito'),
    path('eliminar1/<int:id>', views.eliminar1, name='eliminar1'),
    path('eliminar2/<int:id>', views.eliminar2, name='eliminar2'),
    path('eliminar3/<int:id>', views.eliminar3, name='eliminar3'),
    path('eliminar4/<int:id>', views.eliminar4, name='eliminar4'),
    path('eliminar5/<int:id>', views.eliminar5, name='eliminar5'),
    path('eliminar6/<int:id>', views.eliminar6, name='eliminar6'),
    path('eliminar7/<int:id>', views.eliminar7, name='eliminar7'),
    path('eliminar8/<int:id>', views.eliminar8, name='eliminar8'),
    path('eliminar9/<int:id>', views.eliminar9, name='eliminar9'),
    path('eliminar10/<int:id>', views.eliminar10, name='eliminar10')
]