from django.db import models
from django.contrib.auth.models import User 


class Venta(models.Model):
    id = models.IntegerField(primary_key=True)
    cliente = models.ForeignKey("usuarios.Cliente", verbose_name="Cliente",on_delete= models.DO_NOTHING)
    carrito = models.ForeignKey("carrito.Carrito", verbose_name="Carrito",on_delete= models.DO_NOTHING)
    fecha = models.DateTimeField(auto_now_add=True, blank=True)
    entregada = models.BooleanField(default=False)
    detalle = models.CharField(max_length=500)
    total = models.IntegerField()

