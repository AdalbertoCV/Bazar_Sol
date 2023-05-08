from django.db import models
from django.contrib.auth.models import User 

class Venta(models.Model):
    id = models.IntegerField(primary_key=True)
    cliente = models.ForeignKey("usuarios.Cliente", verbose_name="Cliente",on_delete= models.DO_NOTHING)
    carrito = models.ForeignKey("carrito.Carrito", verbose_name="Carrito",on_delete= models.DO_NOTHING)
    fecha = models.DateTimeField(auto_now_add=True, blank=True)
    entregada = models.BooleanField(default=False)
    articulo1 = models.ForeignKey("articulos.Articulo", on_delete=models.CASCADE, blank=True, null=True, default=None, verbose_name="articulo1_v", related_name="articulo1_v")
    articulo2 = models.ForeignKey("articulos.Articulo", on_delete=models.CASCADE, blank=True, null=True, default=None, verbose_name="articulo2_v", related_name="articulo2_v")
    articulo3 = models.ForeignKey("articulos.Articulo", on_delete=models.CASCADE, blank=True, null=True, default=None, verbose_name="articulo3_v", related_name="articulo3_v")
    articulo4 = models.ForeignKey("articulos.Articulo", on_delete=models.CASCADE, blank=True, null=True, default=None, verbose_name="articulo4_v", related_name="articulo4_v")
    articulo5 = models.ForeignKey("articulos.Articulo", on_delete=models.CASCADE, blank=True, null=True, default=None, verbose_name="articulo5_v", related_name="articulo5_v")
    articulo6 = models.ForeignKey("articulos.Articulo", on_delete=models.CASCADE, blank=True, null=True, default=None, verbose_name="articulo6_v", related_name="articulo6_v")
    articulo7 = models.ForeignKey("articulos.Articulo", on_delete=models.CASCADE, blank=True, null=True, default=None, verbose_name="articulo7_v", related_name="articulo7_v")
    articulo8 = models.ForeignKey("articulos.Articulo", on_delete=models.CASCADE, blank=True, null=True, default=None, verbose_name="articulo8_v", related_name="articulo8_v")
    articulo9 = models.ForeignKey("articulos.Articulo", on_delete=models.CASCADE, blank=True, null=True, default=None, verbose_name="articulo9_v", related_name="articulo9_v")
    articulo10 = models.ForeignKey("articulos.Articulo", on_delete=models.CASCADE, blank=True, null=True, default=None, verbose_name="articulo10_v", related_name="articulo10_v")