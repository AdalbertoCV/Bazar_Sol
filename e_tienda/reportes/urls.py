from django.urls import path
from reportes import views

urlpatterns = [
    path('lista_ventas/', views.ListaVentas, name='lista_ventas'),
    path('buscar_ventas/', views.BuscarVentas, name='buscar_venta'),
    path('reporte_ventas/', views.reporteMensual, name='reporte_venta'),
    path('entregar_ventas/<int:idVenta>', views.entregarVenta, name='entregar_venta'),
    path('descartar_ventas/<int:idVenta>', views.descartarVenta, name='descartar_venta'),
]