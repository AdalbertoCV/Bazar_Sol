from django.db import models
from django.contrib.auth.models import User
from carrito.models import Carrito

class Cliente(models.Model):
    nombre = models.CharField(max_length=150)
    apellido_paterno = models.CharField(max_length=150)
    apellido_materno = models.CharField(max_length=150)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    usuario = models.OneToOneField(User, verbose_name="Usuario", on_delete=models.CASCADE)
    estado = models.ForeignKey("usuarios.Estado", verbose_name="Estado", on_delete=models.DO_NOTHING)
    municipio = models.ForeignKey("usuarios.Municipio", verbose_name="Municipio", on_delete=models.DO_NOTHING)
    direccion = models.CharField(verbose_name="Ingresa tu dirección", max_length=255)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    Carrito = models.ForeignKey("carrito.Carrito", verbose_name="Carrito", on_delete=models.CASCADE, null=True, blank=True)

class Administrador(models.Model):
    nombre = models.CharField(max_length=150)
    apellido_paterno = models.CharField(max_length=150)
    apellido_materno = models.CharField(max_length=150)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    usuario = models.OneToOneField(User, verbose_name="Usuario", on_delete=models.CASCADE)
    estado = models.ForeignKey("usuarios.Estado", verbose_name="Estado", on_delete=models.DO_NOTHING)
    municipio = models.ForeignKey("usuarios.Municipio", verbose_name="Municipio", on_delete=models.DO_NOTHING)
    direccion = models.CharField(verbose_name="Ingresa tu dirección", max_length=255)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    
class Estado(models.Model):
    nombre = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre

class Municipio(models.Model):
    nombre = models.CharField(max_length=100)
    estado = models.ForeignKey("usuarios.Estado", verbose_name="Estado", on_delete=models.DO_NOTHING)
    
    def __str__(self):
        return self.nombre