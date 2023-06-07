from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.models import User, Group
from django.views.generic.edit import CreateView
from .models import Cliente, Administrador, Municipio
from .forms import UserForm, FormPerfilCliente, FormPerfilAdministrador
from django.http import JsonResponse
from django.core.paginator import Paginator
from carrito.models import Carrito
from .models import Administrador
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required


def index(request):
    return render(request, 'base.html')


class RegistrarCliente(SuccessMessageMixin, CreateView):
    model = User
    template_name = 'registrar_cliente.html'
    form_class = UserForm
    success_message = '%(username)s se registró con éxito'
    success_url = reverse_lazy('login')

    #Le asigna por defecto al grupo de cliente
    def form_valid(self, form):
        form = UserForm(self.request.POST)
        if form.is_valid():
            grupo = Group.objects.get(name='cliente')
            user = form.save(commit=False)
            user.is_active = True
            user.save()
            user.groups.add(grupo)
        else:
            return self.render_to_response(self.get_context_data(form=form))
        return super().form_valid(form)  

class RegistrarAdministrador(SuccessMessageMixin, CreateView):
    model = User
    template_name = 'registrar_Administrador.html'
    form_class = UserForm
    success_message = '%(username)s se registró con éxito'
    success_url = reverse_lazy('login')

    #Le asigna por defecto al grupo de administrador
    def form_valid(self, form):
        form = UserForm(self.request.POST)
        if form.is_valid():
            grupo = Group.objects.get(name='administrador')
            user = form.save(commit=False)
            user.is_active = True
            user.save()
            user.groups.add(grupo)
        else:
            return self.render_to_response(self.get_context_data(form=form))
        return super().form_valid(form) 
            

def primera_vez(user):
    #Verificamis si el usuario está iniciando sesión por primera vez
    # Comprobar si el usuario tiene un perfil completo
    perfil = None
    if user.groups.filter(name='administrador').exists():
        try:
            perfil = user.administrador
        except Administrador.DoesNotExist:
            perfil = None
    elif user.groups.filter(name='cliente').exists():
        try:
            perfil = user.cliente
        except Cliente.DoesNotExist:
            perfil = None

    if perfil is None:
        return True

    return False

class LoginView(LoginView):
    template_name = 'login.html'
    form_class = AuthenticationForm

    def post(self, request, *args, **kwargs):
        # Procesar el formulario POST
        form = self.get_form()
        if form.is_valid():
            # Si el formulario es válido, iniciar sesión en la sesión del usuario
            response = self.form_valid(form)
            # Verificar si el usuario está iniciando sesión por primera vez
            user = self.request.user
            if primera_vez(user):
                if user.groups.filter(name='administrador'):
                    return redirect('perfil_admin')
                elif user.groups.filter(name='cliente'):
                    return redirect('perfil_cliente')
            return response
        else:
            # Verificar si el usuario está desactivado
            user = self.request.user
            if not user.is_active:
                messages.warning(request, 'Aún no te haz sido registrado o tu cuenta ha sido desactivada. Por favor registrate, o en caso contrario contacta al administrador.')
            return self.form_invalid(form)

def busca_municipios(request):
    id_estado = request.POST.get('id_estado', None)
    if id_estado:
        municipios = Municipio.objects.filter(estado_id=id_estado)
        data = [{'id':mun.id,'nombre':mun.nombre} for mun in municipios]
        return JsonResponse(data, safe=False)
    return JsonResponse({'error':'Parámetro inválido'}, safe=False)

@permission_required('articulos.permiso_administrador')
def lista_usuarios(request):
    usuarios = User.objects.all()
    grupos = Group.objects.all()
    
    paginator = Paginator(usuarios, 3)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        'object_list':page_obj,
        'page_obj': page_obj,
        'grupos':grupos 
    }
    
    return render(request, 'lista_usuarios.html',context)

@permission_required('articulos.permiso_administrador')
def asignarRoles(request):
    usuarios = request.POST.getlist('usuarios[]')
    if len(usuarios) > 0:
        # asignar roles a los usuarios seleccionados.
        for id in usuarios:
            user = User.objects.get(id=id)
            grupo_id = int(request.POST["grupo"]) # Convertir grupo a un entero
            grupo_nombre = Group.objects.get(id=grupo_id)
            grupoSeleccionado = Group.objects.get(name=grupo_nombre)
            user.groups.add(grupoSeleccionado)
        return redirect('lista_usuarios')
    #simplemente no hace nada, ya que el mensaje de advertencia ya lo mostro el script del formulario
    else:
        return redirect('lista_usuarios')

def EditarUsuario(request, id):
    user = get_object_or_404(User, id=id)
    is_cliente = Group.objects.get(name='cliente') in user.groups.all()

    if request.method == 'POST':
        if is_cliente:
            form = FormPerfilAdministrador(request.POST, instance=user)
        else:
            form = FormPerfilAdministrador(request.POST, instance=user)

        if form.is_valid():
            form.save()
            return redirect('lista_usuarios')
    else:
        if is_cliente:
            form = FormPerfilCliente(instance=user)
        else:
            form = FormPerfilAdministrador(instance=user)

    context = {'form': form}
    return render(request, 'editar_usuario.html', context)

@permission_required('articulos.permiso_administrador')
def EliminarGrupo(request, id):
    user = User.objects.get(id=id)
    if request.method == 'POST':
        grupo_id = request.POST.get('grupo2', '') # Obtener el valor de la opción elegida
        if grupo_id != '':
            grupo_id = int(grupo_id) # Convertir grupo a un entero
            grupoSeleccionado = Group.objects.get(id=grupo_id)
            user.groups.remove(grupoSeleccionado)
            return redirect('lista_usuarios')
        else:
            return redirect('lista_usuarios')

@permission_required('articulos.permiso_administrador')
def AsignarGrupo(request, id):
    user = User.objects.get(id=id)
    if request.method == 'POST':
        grupo_id = request.POST.get('grupo2', '') # Obtener el valor de la opción elegida
        if grupo_id != '':
            grupo_id = int(grupo_id) # Convertir grupo a un entero
            grupoSeleccionado = Group.objects.get(id=grupo_id)
            user.groups.add(grupoSeleccionado)
            return redirect('lista_usuarios')
        else:
            return redirect('lista_usuarios')

@permission_required('articulos.permiso_administrador')
def EliminarUsuario(request, pk):
    usuario = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        usuario.delete()
        return redirect('lista_usuarios')

@permission_required('articulos.permiso_administrador')
def DesactivarUsuario(request, pk):
    usuario = User.objects.get(pk=pk)
    usuario.is_active = False
    usuario.save()
    return redirect('lista_usuarios')
    

def ActivarUsuario(request, pk):
    usuario = User.objects.get(pk=pk)
    usuario.is_active = True
    usuario.save()
    return redirect('lista_usuarios')

def perfil(request):
    # Verificamos si el usuario es administrador
    try:
        administrador = request.user.administrador
        perfil_tipo = 'Administrador'
    except Administrador.DoesNotExist:
        administrador = None

    # Verificamos si el usuario es cliente
    try:
        cliente = request.user.cliente
        perfil_tipo = 'Cliente'
    except Cliente.DoesNotExist:
        cliente = None

    # Si el método de solicitud es POST, procesamos el formulario
    if request.method == 'POST':
        if administrador:
            form = FormPerfilAdministrador(request.POST, request.FILES, instance=administrador)
        elif cliente:
            form = FormPerfilCliente(request.POST, request.FILES, instance=cliente)
        else:
            # Si el usuario no es ni administrador ni cliente, redirigimos a la página de inicio
            return redirect('home')

        if form.is_valid():
            perfil = form.save(commit=False)
            perfil.usuario = request.user
            perfil.save()
            return redirect('home')

    # Si el método de solicitud es GET, mostramos el formulario correspondiente
    else:
        if administrador and isinstance(administrador, Administrador):
            form = FormPerfilAdministrador(instance=administrador)
        elif cliente and isinstance(cliente, Cliente):
            form = FormPerfilCliente(instance=cliente)
        else:
            # Si el usuario no es ni administrador ni cliente, redirigimos a la página de inicio
            return redirect('home')

    context = {
        'form': form,
        'perfil_tipo': perfil_tipo
    }

    return render(request, 'perfil.html', context)

#para rellenar los datos del admin
def perfil_admin(request):
    # verificamos que tipo de perfil accedimos a la tienda
    perfil_tipo = '----'

    form = FormPerfilAdministrador(request.POST, request.FILES)
    if form.is_valid():
        administrador = form.save(commit=False)
        administrador.usuario = request.user
        administrador.save()
        return redirect('home')

    context = {
        'form': form,
        'perfil_tipo': perfil_tipo
    }

    return render(request, 'perfil.html', context)

#para rellenar los datos del cliente
def perfil_cliente(request):
    # verificamos que tipo de perfil accedimos a la tienda
    perfil_tipo = '----'

    form = FormPerfilCliente(request.POST, request.FILES)
    if form.is_valid():
        cliente = form.save(commit=False)
        cliente.usuario = request.user
        cliente.save()
        carrito = Carrito(None,None,None,None,None,None,None,None,None,None)
        carrito.save()
        Cliente.objects.filter(id=cliente.id).update(Carrito = carrito)
        return redirect('home')

    context = {
        'form': form,
        'perfil_tipo': perfil_tipo
    }

    return render(request, 'perfil.html', context)
