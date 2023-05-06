from django.db import models
from .validators import image_validator, directory_path

# Create your models here.
TALLAS = [
    ('UNI', 'Unitalla'),
    ('CH', 'Chica'),
    ('M', 'Mediana'),
    ('G', 'Grande'),
    ('XL', 'Extra Grande'),
]

class Articulo(models.Model):
    id =  models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    talla = models.CharField(max_length=8, choices=TALLAS)
    descripcion = models.TextField(max_length=250, blank=True, null=True)
    imagen = models.ImageField('Foto del Artículo', upload_to=directory_path, validators=[image_validator])

    def __str__(self):
        return f"{self.nombre}"
    
    class Meta:
        ordering = ["id"]
    