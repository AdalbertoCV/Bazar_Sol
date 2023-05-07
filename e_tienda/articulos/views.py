from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Articulo, Resena
from .forms import FormArticulo, FormResena
from django.contrib.auth.decorators import login_required

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
    context={
        'articulo': articulo,
        'resenas':resenas
    }
    return render(request, 'ver_resenas.html', context)

@login_required
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
