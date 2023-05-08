from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from carrito import views

urlpatterns = [
    path('<int:id>', views.VerCarrito, name='ver_carrito'),
    path('agregar_al_carrito/<int:id>/<int:id_carrito>', views.AgregarAlCarrito, name='agregar_al_carrito'),
    path('vaciar_carrito/<int:id>', views.vaciarCarrito, name='vaciar_carrito'),
    path('comprar_carrito/<int:id>', views.comprarCarrito, name='comprar_carrito')
]