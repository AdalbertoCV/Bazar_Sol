from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Articulo, Resena
from .forms import FormArticulo, FormResena
from django.contrib.auth.decorators import login_required, permission_required
import math

# Create your views here.
def lista_articulos(request):
    articulos = Articulo.objects.all()
    paginator = Paginator(articulos, 8) 
    page_request_var = "page"
    page = request.GET.get(page_request_var)
    try:
        articulos = paginator.page(page)
    except PageNotAnInteger:
        articulos = paginator.page(1)
    except EmptyPage:
        articulos = paginator.page(paginator.num_pages)
    context = {
        'object_list': articulos,
        'articulos': articulos,
        'page_request_var': page_request_var,
    }
    return render(request, 'lista_articulos.html', context)

def catalogo_articulos(request):
    articulos = Articulo.objects.all()
    paginator = Paginator(articulos, 8) 
    page_request_var = "page"
    page = request.GET.get(page_request_var)
    try:
        articulos = paginator.page(page)
    except PageNotAnInteger:
        articulos = paginator.page(1)
    except EmptyPage:
        articulos = paginator.page(paginator.num_pages)
    context = {
        'object_list': articulos,
        'articulos': articulos,
        'page_request_var': page_request_var,
    }
    return render(request, 'catalogo_articulos.html', context)

def agregar_articulo(request):
    if request.method == 'POST':
        form = FormArticulo(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_articulos')
    else:
        form = FormArticulo() 
    context = {
        'form': form
    }
    return render(request, 'agregar_articulo.html', context)

def editar_articulo(request, id):
    articulo = Articulo.objects.get(id = id)
    if request.method == 'POST':
        form = FormArticulo(request.POST, instance=articulo)
        if form.is_valid():
            form.save()
            return redirect('lista_articulos')
    else: 
        form = FormArticulo(instance=articulo)
    context = {
        'form': form
    }
    return render(request, 'editar_articulo.html', context)

def eliminar_articulo(request, id):
    Articulo.objects.get(id = id).delete()
    return redirect('lista_articulos')

def VerResenas(request, id):
    resenas = Resena.objects.filter(articulo = id)
    articulo = Articulo.objects.get(id=id)
    vacia = False
    
    if len(resenas) == 0: #Hay reseñas?
        vacia = True
        context = {
            'articulo': articulo,
            'vacia': vacia
        }
    else:
        cont = 0
        suma = 0
        for resena in resenas:
            cont+=1
            suma += int(resena.estrellas)
            
        promedio = suma/cont
        promedioRedondeado = math.floor(promedio)

        #Veremos si el usuario logueado tiene una reseña registrada en el producto
        try:
            resena_usuario = resenas.get(user = request.user)
            hayResena = True
        except:
            hayResena = False
        
        if hayResena:
            
            context={
                'articulo': articulo,
                'resenas':resenas,
                'hayResena':hayResena,
                'resena_usuario':resena_usuario,
                'promedio': promedio,
                'promedioRedondeado': promedioRedondeado,
                'vacia': vacia
            }
        else:
            context={
                'articulo': articulo,
                'resenas':resenas,
                'hayResena':hayResena,
                'promedio': promedio,
                'promedioRedondeado': promedioRedondeado,
                'vacia': vacia
            }

    return render(request, 'ver_resenas.html', context)

def AgregarResena(request, id):
    articulo = Articulo.objects.get(id = id)
    
    if request.method == 'POST':
        form = FormResena(request.POST)
        if form.is_valid():
            form1 = form.save(commit=False)
            form1.articulo = articulo
            form1.user = request.user
            form1.save()
            return redirect('ver_resenas',articulo.id)
    else:
        form = FormResena() 
    context = {
        'form': form
    }
    return render(request, 'agregar_resena.html', context)

def EditarResena(request, id):
    resena = Resena.objects.get(id = id)
    if request.method == 'POST':
        form = FormResena(request.POST, instance=resena)
        if form.is_valid():
            form.save()
            return redirect('ver_resenas',resena.articulo.id)
    else: 
        form = FormResena(instance=resena)
    context = {
        'form': form
    }
    return render(request, 'editar_resena.html', context)


def EliminarResena(request, id):
    id_articulo = Resena.objects.get(id = id).articulo.id
    Resena.objects.get(id = id).delete()
    return redirect('ver_resenas', id_articulo)
