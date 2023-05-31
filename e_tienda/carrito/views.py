from django.shortcuts import render
from .models import Carrito
from articulos.models import Articulo
from usuarios.models import Cliente
from reportes.models import Venta, Detalle
from datetime import datetime as dt
import random as r
from django.contrib import messages
from django.template import Template, Context

def VerCarrito(request,id):
    carrito = Carrito.objects.get(id = id)

    lista=sumarTotal(id)

    total = lista[0]
    cantidad = lista[1]

    context={
        'Carrito': carrito,
        'total': total,
        'cantidad':cantidad
    }
    return render(request, 'ver_carrito.html', context)

from django.contrib import messages

def AgregarAlCarrito(request, id, id_carrito):
    articulos = Articulo.objects.all()
    articulo = Articulo.objects.get(id=id)
    carrito = Carrito.objects.get(id=id_carrito)
    
    carrito_articulo = False
    total = 0

    if carrito.articulo1 is None:
        Carrito.objects.filter(id=id_carrito).update(articulo1=articulo)
        carrito_articulo = True
    elif carrito.articulo2 is None:
        Carrito.objects.filter(id=id_carrito).update(articulo2=articulo)
        carrito_articulo = True
    elif carrito.articulo3 is None:
        Carrito.objects.filter(id=id_carrito).update(articulo3=articulo)
        carrito_articulo = True
    elif carrito.articulo4 is None:
        Carrito.objects.filter(id=id_carrito).update(articulo4=articulo)
        carrito_articulo = True
    elif carrito.articulo5 is None:
        Carrito.objects.filter(id=id_carrito).update(articulo5=articulo)
        carrito_articulo = True
    elif carrito.articulo6 is None:
        Carrito.objects.filter(id=id_carrito).update(articulo6=articulo)
        carrito_articulo = True
    elif carrito.articulo7 is None:
        Carrito.objects.filter(id=id_carrito).update(articulo7=articulo)
        carrito_articulo = True
    elif carrito.articulo8 is None:
        Carrito.objects.filter(id=id_carrito).update(articulo8=articulo)
        carrito_articulo = True
    elif carrito.articulo9 is None:
        Carrito.objects.filter(id=id_carrito).update(articulo9=articulo)
        carrito_articulo = True
    elif carrito.articulo10 is None:
        Carrito.objects.filter(id=id_carrito).update(articulo10=articulo)
        carrito_articulo = True
    
    if carrito_articulo:
        cantidad_articulos = sum(getattr(carrito, f"articulo{i}") is not None for i in range(1, 11))
        messages.success(request, f"Agregaste {cantidad_articulos+1} artículo(s) al carrito.")
    else:
        messages.warning(request, "El carrito está lleno.")
    
    return render(request, 'catalogo_articulos.html', {'articulos': articulos})


    
def vaciarCarrito(request, id):
    carrito = Carrito.objects.get(id = id)
    Carrito.objects.filter(id = id).update(articulo1=None)
    Carrito.objects.filter(id = id).update(articulo2=None)
    Carrito.objects.filter(id = id).update(articulo3=None)
    Carrito.objects.filter(id = id).update(articulo4=None)
    Carrito.objects.filter(id = id).update(articulo5=None)
    Carrito.objects.filter(id = id).update(articulo6=None)
    Carrito.objects.filter(id = id).update(articulo7=None)
    Carrito.objects.filter(id = id).update(articulo8=None)
    Carrito.objects.filter(id = id).update(articulo9=None)
    Carrito.objects.filter(id = id).update(articulo10=None)

    context={
        'Carrito': carrito
    }
    return render(request, 'ver_carrito.html',context)

def sumarTotal(id):
    carrito = Carrito.objects.get(id = id)
    total = 0
    cantidad = 0
    lista = []


    if carrito.articulo1 != None:
        a1 = Articulo.objects.get(id=carrito.articulo1.id)
        total = total + float(a1.precio)
        cantidad = cantidad + 1

    if carrito.articulo2 != None:
        a2 = Articulo.objects.get(id=carrito.articulo2.id)
        total = total + float(a2.precio)
        cantidad = cantidad + 1

    if carrito.articulo3 != None:
        a3 = Articulo.objects.get(id=carrito.articulo3.id)
        total = total + float(a3.precio)
        cantidad = cantidad + 1
    
    if carrito.articulo4 != None:
        a4 = Articulo.objects.get(id=carrito.articulo4.id)
        total = total + float(a4.precio)
        cantidad = cantidad + 1

    if carrito.articulo5 != None:
        a5 = Articulo.objects.get(id=carrito.articulo5.id)
        total = total + float(a5.precio)
        cantidad = cantidad + 1

    if carrito.articulo6 != None:
        a6 = Articulo.objects.get(id=carrito.articulo6.id)
        total = total + float(a6.precio)
        cantidad = cantidad + 1

    if carrito.articulo7 != None:
        a7 = Articulo.objects.get(id=carrito.articulo7.id)
        total = total + float(a7.precio)
        cantidad = cantidad + 1

    if carrito.articulo8 != None:
        a8 = Articulo.objects.get(id=carrito.articulo8.id)
        total = total + float(a8.precio)
        cantidad = cantidad + 1
    
    if carrito.articulo9 != None:
        a9 = Articulo.objects.get(id=carrito.articulo9.id)
        total = total + float(a9.precio)
        cantidad = cantidad + 1

    if carrito.articulo10 != None:
        a10 = Articulo.objects.get(id=carrito.articulo10.id)
        total = total + float(a10.precio)
        cantidad = cantidad + 1

    lista.append(total)
    lista.append(cantidad)

    return lista

def eliminar1(request, id):
    carrito = Carrito.objects.get(id = id)
    carrito = Carrito.objects.filter(id = id).update(articulo1=None)
    carrito = Carrito.objects.get(id = id)
    lista=sumarTotal(id)
    total = lista[0]
    cantidad = lista[1]
    context={
        'Carrito': carrito,
        'total': total,
        'cantidad': cantidad
    }
    return render(request, 'ver_carrito.html',context)

def eliminar2(request, id):
    carrito = Carrito.objects.get(id = id)
    carrito = Carrito.objects.filter(id = id).update(articulo2=None)
    carrito = Carrito.objects.get(id = id)
    lista=sumarTotal(id)
    total = lista[0]
    cantidad = lista[1]
    context={
        'Carrito': carrito,
        'total': total,
        'cantidad': cantidad
    }
    return render(request, 'ver_carrito.html',context)

def eliminar3(request, id):
    carrito = Carrito.objects.get(id = id)
    carrito = Carrito.objects.filter(id = id).update(articulo3=None)
    carrito = Carrito.objects.get(id = id)
    lista=sumarTotal(id)
    total = lista[0]
    cantidad = lista[1]
    context={
        'Carrito': carrito,
        'total': total,
        'cantidad': cantidad
    }
    return render(request, 'ver_carrito.html',context)

def eliminar4(request, id):
    carrito = Carrito.objects.get(id = id)
    Carrito.objects.filter(id = id).update(articulo4=None)
    carrito = Carrito.objects.get(id = id)
    lista=sumarTotal(id)
    total = lista[0]
    cantidad = lista[1]
    context={
        'Carrito': carrito,
        'total': total,
        'cantidad': cantidad
    }
    return render(request, 'ver_carrito.html',context)

def eliminar5(request, id):
    carrito = Carrito.objects.get(id = id)
    Carrito.objects.filter(id = id).update(articulo5=None)
    carrito = Carrito.objects.get(id = id)
    lista=sumarTotal(id)
    total = lista[0]
    cantidad = lista[1]
    context={
        'Carrito': carrito,
        'total': total,
        'cantidad': cantidad
    }
    return render(request, 'ver_carrito.html',context)

def eliminar6(request, id):
    carrito = Carrito.objects.get(id = id)
    Carrito.objects.filter(id = id).update(articulo6=None)
    carrito = Carrito.objects.get(id = id)
    lista=sumarTotal(id)
    total = lista[0]
    cantidad = lista[1]
    context={
        'Carrito': carrito,
        'total': total,
        'cantidad': cantidad
    }
    return render(request, 'ver_carrito.html',context)

def eliminar7(request, id):
    carrito = Carrito.objects.get(id = id)
    Carrito.objects.filter(id = id).update(articulo7=None)
    carrito = Carrito.objects.get(id = id)
    lista=sumarTotal(id)
    total = lista[0]
    cantidad = lista[1]
    context={
        'Carrito': carrito,
        'total': total,
        'cantidad': cantidad
    }
    return render(request, 'ver_carrito.html',context)

def eliminar8(request, id):
    carrito = Carrito.objects.get(id = id)
    Carrito.objects.filter(id = id).update(articulo8=None)
    carrito = Carrito.objects.get(id = id)
    lista=sumarTotal(id)
    total = lista[0]
    cantidad = lista[1]
    context={
        'Carrito': carrito,
        'total': total,
        'cantidad': cantidad
    }
    return render(request, 'ver_carrito.html',context)

def eliminar9(request, id):
    carrito = Carrito.objects.get(id = id)
    Carrito.objects.filter(id = id).update(articulo9=None)
    carrito = Carrito.objects.get(id = id)
    lista=sumarTotal(id)
    total = lista[0]
    cantidad = lista[1]
    context={
        'Carrito': carrito,
        'total': total,
        'cantidad': cantidad
    }
    return render(request, 'ver_carrito.html',context)

def eliminar10(request, id):
    carrito = Carrito.objects.get(id = id)
    Carrito.objects.filter(id = id).update(articulo10=None)
    carrito = Carrito.objects.get(id = id)
    lista=sumarTotal(id)
    total = lista[0]
    cantidad = lista[1]
    context={
        'Carrito': carrito,
        'total': total,
        'cantidad': cantidad
    }
    return render(request, 'ver_carrito.html',context)

def comprarCarrito(request, id):
    cliente = Cliente.objects.get(id=id)
    carrito = Carrito.objects.get(id=cliente.Carrito.id)
    idCarrito = carrito.id

    codigo = 0
    existe = True
    while existe:
        codigo = r.randrange(1000000, 9999999, 1)
        try:
            Venta.objects.get(id=codigo)
        except:
            existe=False
    total = 0
    try:
        a1 = Articulo.objects.get(id=carrito.articulo1.id)
        total = total + float(a1.precio)
    except:
        a1 = None
    try:
        a2 = Articulo.objects.get(id=carrito.articulo2.id)
        total = total + float(a2.precio)
    except:
        a2 = None
    try:
        a3 = Articulo.objects.get(id=carrito.articulo3.id)
        total = total + float(a3.precio)
    except:
        a3= None
    try:
        a4 = Articulo.objects.get(id=carrito.articulo4.id)
        total = total + float(a4.precio)
    except:
        a4 = None
    try:
        a5 = Articulo.objects.get(id=carrito.articulo5.id)
        total = total + float(a5.precio)
    except:
        a5=None
    try:
        a6 = Articulo.objects.get(id=carrito.articulo6.id)
        total = total + float(a6.precio)
    except:
        a6=None
    try:
        a7 = Articulo.objects.get(id=carrito.articulo7.id)
        total = total + float(a7.precio)
    except:
        a7=None
    try:
        a8 = Articulo.objects.get(id=carrito.articulo8.id)
        total = total + float(a8.precio)
    except:
        a8=None
    try:
        a9 = Articulo.objects.get(id=carrito.articulo9.id)
        total = total + float(a9.precio)
    except:
        a9=None
    try:
        a10 = Articulo.objects.get(id=carrito.articulo10.id)
        total = total + float(a10.precio)
    except:
        a10=None

    new_values = {"id": codigo, "cliente": cliente, "carrito":carrito,'fecha': dt.now(),'entregada': False, 'total': total}
    obj = Venta(**new_values)
    obj.save()

    ventaActual = Venta.objects.get(id=codigo)

    if a1:
        new_values = {"id_venta": ventaActual, "articulo": a1}
        d = Detalle(**new_values)
        d.save()
    if a2:
        new_values = {"id_venta": ventaActual, "articulo": a2}
        d = Detalle(**new_values)
        d.save()
    if a3:
        new_values = {"id_venta": ventaActual, "articulo": a3}
        d = Detalle(**new_values)
        d.save()
    if a4:
        new_values = {"id_venta": ventaActual, "articulo": a4}
        d = Detalle(**new_values)
        d.save()
    if a5:
        new_values = {"id_venta": ventaActual, "articulo": a5}
        d = Detalle(**new_values)
        d.save()
    if a6:
        new_values = {"id_venta": ventaActual, "articulo": a6}
        d = Detalle(**new_values)
        d.save()
    if a7:
        new_values = {"id_venta": ventaActual, "articulo": a7}
        d = Detalle(**new_values)
        d.save()
    if a8:
        new_values = {"id_venta": ventaActual, "articulo": a8}
        d = Detalle(**new_values)
        d.save()
    if a9:
        new_values = {"id_venta": ventaActual, "articulo": a9}
        d = Detalle(**new_values)
        d.save()
    if a10:
        new_values = {"id_venta": ventaActual, "articulo": a10}
        d = Detalle(**new_values)
        d.save()
    vaciar(idCarrito)
    return render(request,'codigo.html', {'codigo':codigo})

def vaciar(id):
    Carrito.objects.filter(id = id).update(articulo1=None)
    Carrito.objects.filter(id = id).update(articulo2=None)
    Carrito.objects.filter(id = id).update(articulo3=None)
    Carrito.objects.filter(id = id).update(articulo4=None)
    Carrito.objects.filter(id = id).update(articulo5=None)
    Carrito.objects.filter(id = id).update(articulo6=None)
    Carrito.objects.filter(id = id).update(articulo7=None)
    Carrito.objects.filter(id = id).update(articulo8=None)
    Carrito.objects.filter(id = id).update(articulo9=None)
    Carrito.objects.filter(id = id).update(articulo10=None)