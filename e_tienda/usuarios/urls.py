from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('nuevo_cliente/', views.RegistrarCliente.as_view(), name='nuevo_cliente'),
    path('nuevo_administrador/', views.RegistrarAdministrador.as_view(), name='nuevo_admin'),
    path('index/', views.index, name='index_nu'),
    path('municipios/', views.busca_municipios, name='busca_municipios'),
    path('lista',views.lista_usuarios, name='lista_usuarios'),
    path('asignar-usuarios', views.asignarRoles, name='asignar_usuarios'),
    path('editar/<int:id>', views.EditarUsuario, name='editar_usuario'),
    path('eliminar-grupo/<int:id>', views.EliminarGrupo, name='eliminar_grupo'),
    path('asignarGrupo/<int:id>', views.AsignarGrupo, name='asignar_grupo'),
    path('eliminar-usuario/<int:pk>/', views.EliminarUsuario, name='eliminar_usuario'),
    path('desactivar-usuario/<int:pk>/', views.DesactivarUsuario, name='desactivar_usuario'),
    path('activar-usuario/<int:pk>/', views.ActivarUsuario, name='activar_usuario'),
    path('perfil', views.perfil, name='perfil_usuario'),
    path('perfil_administrador', views.perfil_admin, name='perfil_admin'),
    path('perfil_cliente', views.perfil_cliente, name='perfil_cliente')
]