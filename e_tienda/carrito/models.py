from django.db import models
from articulos.models import Articulo

class Carrito(models.Model):
    id =  models.AutoField(primary_key=True)
    articulo1 = models.ForeignKey("articulos.Articulo", on_delete=models.CASCADE, blank=True, null=True, default=None, verbose_name="articulo1", related_name="articulo1")
    articulo2 = models.ForeignKey("articulos.Articulo", on_delete=models.CASCADE, blank=True, null=True, default=None, verbose_name="articulo2", related_name="articulo2")
    articulo3 = models.ForeignKey("articulos.Articulo", on_delete=models.CASCADE, blank=True, null=True, default=None, verbose_name="articulo3", related_name="articulo3")
    articulo4 = models.ForeignKey("articulos.Articulo", on_delete=models.CASCADE, blank=True, null=True, default=None, verbose_name="articulo4", related_name="articulo4")
    articulo5 = models.ForeignKey("articulos.Articulo", on_delete=models.CASCADE, blank=True, null=True, default=None, verbose_name="articulo5", related_name="articulo5")
    articulo6 = models.ForeignKey("articulos.Articulo", on_delete=models.CASCADE, blank=True, null=True, default=None, verbose_name="articulo6", related_name="articulo6")
    articulo7 = models.ForeignKey("articulos.Articulo", on_delete=models.CASCADE, blank=True, null=True, default=None, verbose_name="articulo7", related_name="articulo7")
    articulo8 = models.ForeignKey("articulos.Articulo", on_delete=models.CASCADE, blank=True, null=True, default=None, verbose_name="articulo8", related_name="articulo8")
    articulo9 = models.ForeignKey("articulos.Articulo", on_delete=models.CASCADE, blank=True, null=True, default=None, verbose_name="articulo9", related_name="articulo9")
    articulo10 = models.ForeignKey("articulos.Articulo", on_delete=models.CASCADE, blank=True, null=True, default=None, verbose_name="articulo10", related_name="articulo10")