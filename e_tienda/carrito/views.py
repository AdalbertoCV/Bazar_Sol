from django.shortcuts import render
from .models import Carrito
from articulos.models import Articulo
from usuarios.models import Cliente
from reportes.models import Venta
from datetime import datetime as dt
import random as r

def VerCarrito(request,id):
    carrito = Carrito.objects.get(id = id)
    context={
        'Carrito': carrito
    }
    return render(request, 'ver_carrito.html', context)

def AgregarAlCarrito(request, id, id_carrito):
    articulos = Articulo.objects.all()
    articulo = Articulo.objects.get(id = id)
    carrito = Carrito.objects.get(id = id_carrito)

    if carrito.articulo1 == None:
        Carrito.objects.filter(id = id_carrito).update(articulo1=articulo)
    elif carrito.articulo2 == None:
        Carrito.objects.filter(id = id_carrito).update(articulo2=articulo)
    elif carrito.articulo3 == None:
        Carrito.objects.filter(id = id_carrito).update(articulo3=articulo)
    elif carrito.articulo4 == None:
        Carrito.objects.filter(id = id_carrito).update(articulo4=articulo)
    elif carrito.articulo5 == None:
        Carrito.objects.filter(id = id_carrito).update(articulo5=articulo)
    elif carrito.articulo6 == None:
        Carrito.objects.filter(id = id_carrito).update(articulo6=articulo)
    elif carrito.articulo7 == None:
        Carrito.objects.filter(id = id_carrito).update(articulo7=articulo)
    elif carrito.articulo8 == None:
        Carrito.objects.filter(id = id_carrito).update(articulo8=articulo)
    elif carrito.articulo9 == None:
        Carrito.objects.filter(id = id_carrito).update(articulo9=articulo)
    elif carrito.articulo10 == None:
        Carrito.objects.filter(id = id_carrito).update(articulo10=articulo)

    return render(request, 'catalogo_articulos.html', {'articulos':articulos})

    
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
        'carrito': carrito
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
    
    try:
        a1 = Articulo.objects.get(id=carrito.articulo1.id)
    except:
        a1 = None
    try:
        a2 = Articulo.objects.get(id=carrito.articulo2.id)
    except:
        a2 = None
    try:
        a3 = Articulo.objects.get(id=carrito.articulo3.id)
    except:
        a3= None
    try:
        a4 = Articulo.objects.get(id=carrito.articulo4.id)
    except:
        a4 = None
    try:
        a5 = Articulo.objects.get(id=carrito.articulo5.id)
    except:
        a5=None
    try:
        a6 = Articulo.objects.get(id=carrito.articulo6.id)
    except:
        a6=None
    try:
        a7 = Articulo.objects.get(id=carrito.articulo7.id)
    except:
        a7=None
    try:
        a8 = Articulo.objects.get(id=carrito.articulo8.id)
    except:
        a8=None
    try:
        a9 = Articulo.objects.get(id=carrito.articulo9.id)
    except:
        a9=None
    try:
        a10 = Articulo.objects.get(id=carrito.articulo10.id)
    except:
        a10=None

    new_values = {"id": codigo, "cliente": cliente, "carrito":carrito,'fecha': dt.now(), 'entregada': False, 
                  'articulo1':a1,'articulo2':a2,'articulo3':a3,'articulo4':a4,'articulo5':a5,
                  'articulo6':a6,'articulo7':a7,'articulo8':a8,'articulo9':a9,'articulo10':a10}
    obj = Venta(**new_values)
    obj.save()
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