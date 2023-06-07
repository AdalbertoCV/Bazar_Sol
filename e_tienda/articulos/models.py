from django.db import models
from .validators import image_validator, directory_path
from django.core.validators import RegexValidator
from django.contrib.auth.models import User


# Create your models here.
TALLAS = [
    ('UNI', 'Unitalla'),
    ('CH', 'Chica'),
    ('M', 'Mediana'),
    ('G', 'Grande'),
    ('XL', 'Extra Grande'),
]

ESTRELLAS = [
    ('', 'No estrellas'),
    ('1','1 Estrella'),
    ('2','2 Estrellas'),
    ('3','3 Estrellas'),
    ('4','4 Estrellas'),
    ('5','5 Estrellas'),
]

class Articulo(models.Model):
    id =  models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100,validators=[RegexValidator('[+-/%]', inverse_match=True)])
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    talla = models.CharField(max_length=8, choices=TALLAS)
    descripcion = models.TextField(max_length=250, blank=True, null=True)
    imagen = models.ImageField('Foto del Artículo', upload_to=directory_path, validators=[image_validator], default=None)
    imagen2 = models.ImageField('Foto del Artículo 2', upload_to=directory_path, validators=[image_validator], default=None)
    imagen3 = models.ImageField('Foto del Artículo 3', upload_to=directory_path, validators=[image_validator], default=None)
    imagen4 = models.ImageField('Foto del Artículo 4', upload_to=directory_path, validators=[image_validator], default=None)
    imagen5 = models.ImageField('Foto del Artículo 5', upload_to=directory_path, validators=[image_validator], default=None)
    
    def __str__(self):
        return f"{self.nombre}"
    
    class Meta:
        ordering = ["id"]

class Resena(models.Model):
    descripcion = models.TextField(max_length=500)
    estrellas = models.CharField(max_length=12,choices=ESTRELLAS)
    fecha = models.DateField(auto_now_add=True)
    articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} - {self.fecha}"