from django.shortcuts import render
from .models import Venta, Detalle
from articulos.models import Articulo
from usuarios.models import Cliente
import datetime
from collections import Counter
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import random as r
from datetime import datetime as dt
from django.views.generic import TemplateView
from django.db.models import Count
from django.contrib.auth.decorators import login_required, permission_required

@permission_required('articulos.permiso_administrador')
def ListaVentas(request):
    ventas = Venta.objects.all()
    paginator = Paginator(ventas, 5) 
    page_request_var = "page"
    page = request.GET.get(page_request_var)
    try:
        ventas = paginator.page(page)
    except PageNotAnInteger:
        ventas = paginator.page(1)
    except EmptyPage:
        ventas = paginator.page(paginator.num_pages)
    context = {'object_list': ventas,'Ventas': ventas,'page_request_var': page_request_var}
    return render(request, 'reportes/venta_list.html', context)

@permission_required('articulos.permiso_administrador')
def BuscarVentas(request):
    ventas = Venta.objects.all()
    if request.method == 'POST':
        id = request.POST.get('id',None)
        cliente = request.POST.get('cliente',None)
        inicio = request.POST.get('inicio',None)
        fin= request.POST.get('fin',None)
        entregada = request.POST.get('entregada', None)

        if inicio and fin:
            diaInicio = inicio[8] + inicio[9]
            mesInicio = inicio[5] + inicio[6]
            anioInicio = inicio[0] + inicio[1] +inicio[2] + inicio[3]
            diaFin = fin[8] + fin[9]
            mesFin = fin[5] + fin[6]
            anioFin = fin[0] + fin[1] + fin[2] + fin[3]
            ventas = Venta.objects.filter(fecha__gte=datetime.date(int(anioInicio),int(mesInicio), int(diaInicio)),
                                fecha__lte=datetime.date(int(anioFin), int(mesFin), int(diaFin)))
        elif inicio:
            diaInicio = inicio[8] + inicio[9]
            mesInicio = inicio[5] + inicio[6]
            anioInicio = inicio[0] + inicio[1] +inicio[2] + inicio[3]
            ventas = Venta.objects.filter(fecha__gte=datetime.date(int(anioInicio),int(mesInicio), int(diaInicio)),
                                fecha__lte=datetime.date(2050, 1, 1))
        elif fin:
            diaFin = fin[8] + fin[9]
            mesFin = fin[5] + fin[6]
            anioFin = fin[0] + fin[1] + fin[2] + fin[3]
            ventas = Venta.objects.filter(fecha__gte=datetime.date(2000,1, 1),
                                fecha__lte=datetime.date(int(anioFin), int(mesFin), int(diaFin)))
        if id:
            ventas =ventas.filter(id =id)
        if cliente:
            ventas = ventas.filter(cliente__id = cliente)
        if entregada == '1':
            ventas = ventas.filter(entregada= True)
        elif entregada=='2':
            ventas = ventas.filter(entregada= False)
    paginator = Paginator(ventas, 5) 
    page_request_var = "page"
    page = request.GET.get(page_request_var)
    try:
        ventas = paginator.page(page)
    except PageNotAnInteger:
        ventas = paginator.page(1)
    except EmptyPage:
        ventas = paginator.page(paginator.num_pages)
    context = {'object_list': ventas,'Ventas': ventas,'page_request_var': page_request_var}
    return render(request, 'reportes/venta_list.html', context)

@permission_required('articulos.permiso_administrador')
def reporteMensual(request):
    top_clientes = []
    top_productos = []
    total_ventas = 0
    if request.method == 'POST':
        mes = request.POST.get('mes',None)
        anio = request.POST.get('año', None)
        if mes == 1:
            ventas = Venta.objects.filter(fecha__gte=datetime.date(int(anio),int(mes), 1),
                                fecha__lte=datetime.date(int(anio), int(mes), 28), entregada=True)
        else:
            ventas = Venta.objects.filter(fecha__gte=datetime.date(int(anio),int(int(mes)-1), 28),
                                fecha__lte=datetime.date(int(anio), int(mes), 28),entregada=True)
        clientes = []
        productos = []
        for venta in ventas:
            total_ventas = total_ventas + float(venta.total)
            clientes.append(venta.cliente.id)
            articulos = Detalle.objects.filter(id_venta = venta.id)
            for articulo in articulos:
                productos.append(articulo.articulo.id)
        counter_cli = Counter(clientes)
        counter_prod = Counter(productos)
        clientes_orde = counter_cli.most_common()
        productos_orde = counter_prod.most_common()
        
        if (len(clientes_orde) >10):
            top_prod = productos_orde[0:9]
        else:
            top_cli = clientes_orde

        if (len(productos_orde)>10):
            top_prod = productos_orde[0:9]
        else:
            top_prod = productos_orde
        
        for cliente in top_cli:
            ClienteActual = Cliente.objects.get(id=int(cliente[0]))
            top_clientes.append(ClienteActual.nombre)
        for producto in top_prod:
            ProductoActual = Articulo.objects.get(id=int(producto[0]))
            top_productos.append(ProductoActual.nombre)

    context = {'clientes':top_clientes,'productos':top_productos ,'Total': total_ventas}
    return render(request, 'reportes/reporte.html', context)

@permission_required('art.iculos.permiso_administrador')
def entregarVenta(request, idVenta):
    ventas = Venta.objects.all()
    Venta.objects.filter(id=idVenta).update(entregada=True)
    return render(request, 'reportes/venta_list.html', {'Ventas':ventas})

@permission_required('articulos.permiso_administrador')
def descartarVenta(request, idVenta):
    ventas = Venta.objects.all()
    Venta.objects.filter(id=idVenta).delete()
    return render(request, 'reportes/venta_list.html', {'Ventas':ventas})

class graficas(TemplateView):
    template_name = 'reportes/graficas.html'
    detalles_ventas = Detalle.objects.all().values('articulo').annotate(cuantos = Count('articulo'))
    articulos = Articulo.objects.all()

    datosArt = []

    for a in articulos:
        cuantos = 0
        for dv in detalles_ventas:
            if dv['articulo'] == a.id:
                cuantos = dv['cuantos']
                break
        datosArt.append({'name':a.nombre,'data':[cuantos]})
    extra_context = {'datosArticulos': datosArt}
    


